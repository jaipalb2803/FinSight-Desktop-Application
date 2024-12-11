import os
import sys
import datetime
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6.QtGui import QStandardItemModel, QStandardItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import json
from matplotlib.colors import to_hex
import tempfile  # To create a temporary file
import requests
from datetime import datetime, timedelta
from windows_ui.Investment_Portfolio import Ui_Investment_Portfolio
from fpdf import FPDF
from pathlib import Path

class DataExtractor:
    def __init__(self, raw_response_file, insights_file, historical_data_file):
        self.raw_response_file = raw_response_file
        self.insights_file = insights_file
        self.historical_data_file = historical_data_file

    def _load_raw_response(self):
        """Load raw responses from the JSON file."""
        if not os.path.exists(self.raw_response_file):
            print("Raw response file does not exist.")
            return {}
        try:
            with open(self.raw_response_file, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Failed to load raw responses: {e}")
            return {}

    def _save_insights(self, insights):
        """Save insights to a text file."""
        try:
            with open(self.insights_file, "w") as file:
                for key, value in insights.items():
                    file.write(f"{key}:\n")
                    if isinstance(value, list):
                        for item in value:
                            file.write(f"  - {item}\n")
                    elif isinstance(value, dict):
                        for subkey, subvalue in value.items():
                            file.write(f"  {subkey}: {subvalue}\n")
                    else:
                        file.write(f"  {value}\n")
                    file.write("\n")
            print(f"Insights saved to {self.insights_file}")
        except Exception as e:
            print(f"Failed to save insights: {e}")

    def _save_historical_data(self, historical_data, api_call_time):
        """Save historical price data to a JSON file."""
        try:
            # Load existing historical data
            if os.path.exists(self.historical_data_file):
                with open(self.historical_data_file, "r") as file:
                    existing_data = json.load(file)
            else:
                existing_data = []

            # Append the new data with a timestamp
            new_entry = {"timestamp": api_call_time, "prices": historical_data}
            existing_data.append(new_entry)

            # Save back to the file
            with open(self.historical_data_file, "w") as file:
                json.dump(existing_data, file, indent=4)
            print(f"Historical data updated in {self.historical_data_file}")
        except Exception as e:
            print(f"Failed to save historical data: {e}")

    def extract_data(self):
        """Extract all showcaseable information from the raw response."""
        raw_data = self._load_raw_response()
        if not raw_data:
            print("No raw data to process.")
            return

        # Use the current timestamp for historical data
        api_call_time = datetime.now().isoformat()

        insights = {}
        historical_data = {}

        for asset_name, response in raw_data.items():
            if "error" in response:
                insights[asset_name] = {"error": response["error"]}
                continue

            asset_insights = {}

            # Extract price graph data
            if "graph" in response:
                last_price = response["graph"][-1]
                price = last_price.get("price")
                currency = last_price.get("currency")
                if price is not None:
                    historical_data[asset_name] = {"price": price, "currency": currency}

            # Extract knowledge graph data
            if "knowledge_graph" in response:
                knowledge = response["knowledge_graph"].get("about", {})
                asset_insights["knowledge_graph"] = {
                    "Company": knowledge.get("company"),
                    "Description": knowledge.get("description"),
                    "CEO": knowledge.get("ceo"),
                    "Founded": knowledge.get("founded"),
                    "Employees": knowledge.get("employees"),
                    "Website": knowledge.get("website"),
                    "Wikipedia": knowledge.get("wikipedia"),
                }

            # Extract compared assets insights
            if "compare_to" in response:
                comparisons = []
                for comparison in response["compare_to"]:
                    comparisons.append({
                        "Stock": comparison.get("stock"),
                        "Company": comparison.get("company"),
                        "Price": comparison.get("price"),
                        "Price Change %": comparison.get("price_change", {}).get("percentage"),
                        "Movement": comparison.get("price_change", {}).get("movement"),
                        "Date": comparison.get("date"),
                    })
                asset_insights["comparisons"] = comparisons

            # Extract news articles or other highlights (if available)
            if "articles" in response:
                articles = []
                for article in response["articles"]:
                    articles.append({
                        "Title": article.get("title"),
                        "URL": article.get("url"),
                        "Source": article.get("source"),
                    })
                asset_insights["articles"] = articles

            # Extract market data (if available)
            if "markets" in response:
                asset_insights["markets"] = response["markets"]

            # Save extracted insights
            insights[asset_name] = asset_insights

        # Save insights and historical data
        self._save_insights(insights)
        self._save_historical_data(historical_data, api_call_time)
        print("Data extraction completed.")
        
class APIHandler:
    def __init__(self, assets_file, raw_response_file, api_key, timestamp_file, historical_prices_file, api_url="https://www.searchapi.io/api/v1/search"):
        self.assets_file = assets_file
        self.raw_response_file = raw_response_file
        self.timestamp_file = timestamp_file
        self.historical_prices_file = historical_prices_file
        self.api_key = api_key
        self.api_url = api_url
        self.gate_interval = timedelta(hours=8)  # 8-hour interval for gating API calls

    def _read_assets(self):
        """Read asset names from the CSV file."""
        if not os.path.exists(self.assets_file):
            print("Assets CSV file does not exist.")
            return []
        try:
            data = pd.read_csv(self.assets_file)
            return data["Name"].tolist()
        except Exception as e:
            print(f"Error reading assets CSV: {e}")
            return []

    def _get_last_call_timestamp(self):
        """Retrieve the last API call timestamp from the file."""
        if not os.path.exists(self.timestamp_file):
            return None
        try:
            with open(self.timestamp_file, "r") as file:
                timestamp = file.read().strip()
                return datetime.fromisoformat(timestamp)
        except Exception as e:
            print(f"Error reading timestamp file: {e}")
            return None

    def _is_gate_open(self):
        """Check if the 8-hour gating period has passed."""
        last_call_timestamp = self._get_last_call_timestamp()
        if last_call_timestamp is None:
            return True
        return datetime.now() >= last_call_timestamp + self.gate_interval

    def _update_last_call_timestamp(self):
        """Update the last API call timestamp in the file."""
        try:
            with open(self.timestamp_file, "w") as file:
                file.write(datetime.now().isoformat())
        except Exception as e:
            print(f"Error updating timestamp file: {e}")

    def _fetch_asset_data(self, asset_name):
        """Fetch data for a single asset."""
        try:
            params = {
                "engine": "google_finance",
                "q": asset_name,
                "api_key": self.api_key
            }
            response = requests.get(self.api_url, params=params)
            if response.status_code == 200:
                return asset_name, response.json()
            else:
                return asset_name, {"error": f"Status code {response.status_code}"}
        except Exception as e:
            return asset_name, {"error": str(e)}

    def fetch_all_assets(self):
        """Fetch data for all assets in parallel and save the results."""
        if not self._is_gate_open():
            print("API calls are gated for 8 hours. No API call made.")
            return None

        assets = self._read_assets()
        if not assets:
            print("No assets found.")
            return None

        from concurrent.futures import ThreadPoolExecutor

        print("Fetching data for assets...")
        results = {}
        with ThreadPoolExecutor() as executor:
            futures = {executor.submit(self._fetch_asset_data, asset): asset for asset in assets}
            for future in futures:
                asset_name = futures[future]
                try:
                    asset_name, data = future.result()
                    results[asset_name] = data
                except Exception as e:
                    results[asset_name] = {"error": str(e)}

        # Save raw responses to a JSON file (overwriting existing data)
        self._save_raw_responses(results)

        # Update last API call timestamp
        self._update_last_call_timestamp()
        print("API call completed and data saved successfully.")
        return results

    def _save_raw_responses(self, data):
        """Save raw responses to a JSON file."""
        try:
            with open(self.raw_response_file, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Raw responses saved to {self.raw_response_file}")
        except Exception as e:
            print(f"Failed to save raw responses: {e}")

    def load_raw_responses(self):
        """Load raw responses from the JSON file."""
        if not os.path.exists(self.raw_response_file):
            print("Raw response file does not exist.")
            return {}
        try:
            with open(self.raw_response_file, "r") as file:
                return json.load(file)
        except Exception as e:
            print(f"Failed to load raw responses: {e}")
            return {}

    def update_asset_prices(self):
        """Update asset prices in the CSV file using the latest prices from the historical prices JSON file."""
        if not os.path.exists(self.historical_prices_file):
            print("Historical prices file does not exist. Cannot update prices.")
            return

        # Load historical prices
        try:
            with open(self.historical_prices_file, "r") as file:
                historical_data = json.load(file)
        except Exception as e:
            print(f"Failed to load historical prices file: {e}")
            return

        # Load assets from the CSV file
        if not os.path.exists(self.assets_file):
            print("Assets CSV file does not exist.")
            return

        try:
            assets_df = pd.read_csv(self.assets_file)
        except Exception as e:
            print(f"Failed to read assets CSV: {e}")
            return

        # Update prices based on the latest historical data
        updated_rows = []
        for _, row in assets_df.iterrows():
            asset_name = row["Name"]
            quantity = row.get("Quantity", 0)

            # Retrieve the latest price for the asset
            latest_price = None
            for record in reversed(historical_data):  # Iterate through historical data (latest first)
                if asset_name in record.get("prices", {}):
                    latest_price = record["prices"][asset_name].get("price")
                    break

            if latest_price is not None:
                total_value = latest_price * quantity
                row["Price"] = round(total_value, 2)  # Update the price column
            else:
                print(f"No historical price data available for asset: {asset_name}")

            updated_rows.append(row)

        # Save the updated rows back to the CSV
        try:
            updated_df = pd.DataFrame(updated_rows)
            updated_df.to_csv(self.assets_file, index=False)
            print("Asset prices updated successfully.")
        except Exception as e:
            print(f"Failed to save updated assets CSV: {e}")

class LegendDialog(qtw.QDialog):
    """Custom dialog to display the graph legend."""
    def __init__(self, parent, colors):
        super().__init__(parent)
        self.setWindowTitle("Graph Legend")
        self.setFixedSize(300, 400)

        layout = qtw.QVBoxLayout()
        title_label = qtw.QLabel("<h3>Asset Legend</h3>")
        layout.addWidget(title_label)

        for asset, color in colors.items():
            legend_item = qtw.QLabel(f"<span style='color:{color}; font-size: 16px;'>■</span> {asset}")
            layout.addWidget(legend_item)

        close_button = qtw.QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)
        self.setLayout(layout)

class InvestmentPortfolioApp(qtw.QMainWindow, Ui_Investment_Portfolio):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Ensure f_Progress_Line_Graph has a layout
        if not self.f_Progress_Line_Graph.layout():
            layout = qtw.QVBoxLayout()
            self.f_Progress_Line_Graph.setLayout(layout)

        # Matplotlib figure setup
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.f_Progress_Line_Graph.layout().addWidget(self.canvas)

        # Base directory setup
        base_directory = Path(__file__).resolve().parent
        self.assets_directory = base_directory / "data storage" / "assets"
        self.assets_directory.mkdir(parents=True, exist_ok=True)

        # Define all file paths relative to the base directory
        self.asset_file = self.assets_directory / "assets.csv"
        self.raw_response_file = self.assets_directory / "raw_responses.json"
        self.historical_prices_file = self.assets_directory / "historical_prices.json"
        self.timestamp_file = self.assets_directory / "last_call_timestamp.txt"
        self.insights_file = self.assets_directory / "insights.txt"
        self.log_file = base_directory / "logs" / "application.log"
        self.pdf_directory = base_directory / "data storage" / "pdf"
        self.pdf_directory.mkdir(parents=True, exist_ok=True)
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.api_key = "ENTER API KEY"  # Replace with your API key
        self.api_url = "https://www.searchapi.io/api/v1/search"

        # Initialize assets CSV
        self.initialize_assets_csv()

        # Data model for the asset table
        self.asset_model = QStandardItemModel(0, 6)
        self.asset_model.setHorizontalHeaderLabels(
            ["Type", "Name", "Subcategory", "Quantity", "Quantity Type", "Price"]
        )
        self.tv_Assets_Status_Display.setModel(self.asset_model)

        # Initialize APIHandler and DataExtractor
        self.api_handler = APIHandler(
            self.asset_file,
            self.raw_response_file,
            self.api_key,
            self.timestamp_file,
            self.historical_prices_file,
            self.api_url
        )
        self.data_extractor = DataExtractor(
            self.raw_response_file,
            self.insights_file,
            self.historical_prices_file
        )

        # Asset category mapping
        self.asset_data = {
            "Stock": {"subcategories": ["NASDAQ", "NYSE"], "names": ["NVDA:NASDAQ", "AAPL:NASDAQ", "MSFT:NASDAQ"]},
            "Mutual Funds": {"subcategories": ["Growth", "Value"], "names": ["VTSAX:MUTF", "FZROX:MUTF"]},
            "Currency": {"subcategories": ["Crypto", "Fiat"], "names": ["BTC-USD"]},
        }

        self.quantity_mapping = {
            "Stock": "Units",
            "Mutual Funds": "Shares",
            "Currency": "Lots",
        }

        # UI signal connections
        self.cb_Asset_Types.currentIndexChanged.connect(self.update_subcategories_and_names)
        self.pb_Add_Asset.clicked.connect(self.add_asset)
        self.pb_Remove_Asset.clicked.connect(self.remove_asset)
        self.pb_Extract_Portfolio.clicked.connect(self.extract_portfolio)

        # Load existing data and check API operations
        self.load_existing_data()
        self.run_api_operations()

        # Refresh graph and display insights
        self.refresh_graph()
        self.display_insights()

        # Initialize and show the legend dialog
        self.legend_dialog = None  # Ensure the legend_dialog is initialized

    def run_api_operations(self):
        """Run API fetch and extraction operations if the 8-hour condition is met."""
        if self.api_handler._is_gate_open():
            self.log_status("Starting API operations...")
            self.api_handler.fetch_all_assets()  # Fetch new data
            self.data_extractor.extract_data()  # Extract insights and historical data
            self.api_handler.update_asset_prices()  # Update asset prices from historical data
            self.log_status("API operations completed.")
        else:
            self.log_status("API calls are gated. Continuing with existing data.")

    def log_status(self, message):
        """Log messages to a file."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        with open(self.log_file, "a") as log_file:
            log_file.write(log_message + "\n")
        self.l_Status.setText(message)

    def initialize_assets_csv(self):
        if not os.path.exists(self.asset_file):
            pd.DataFrame(columns=["Type", "Name", "Subcategory", "Quantity", "Quantity Type", "Price"]).to_csv(
                self.asset_file, index=False
            )

    def load_existing_data(self):
        try:
            data = pd.read_csv(self.asset_file)
            for _, row in data.iterrows():
                self.asset_model.appendRow([
                    QStandardItem(row["Type"]),
                    QStandardItem(row["Name"]),
                    QStandardItem(row["Subcategory"]),
                    QStandardItem(str(row["Quantity"])),
                    QStandardItem(row["Quantity Type"]),
                    QStandardItem(str(row.get("Price", ""))),
                ])
            self.log_status("Assets loaded successfully.")
        except Exception as e:
            self.log_status(f"Failed to load assets: {e}")

    def update_subcategories_and_names(self):
        asset_type = self.cb_Asset_Types.currentText()
        if asset_type in self.asset_data:
            subcategories = self.asset_data[asset_type]["subcategories"]
            names = self.asset_data[asset_type]["names"]

            self.cb_Sub_Category_Selection.clear()
            self.cb_Sub_Category_Selection.addItems(subcategories)

            self.cb_Asset_Name.clear()
            self.cb_Asset_Name.addItems(names)

            self.l_Quantitative_Category.setText(self.quantity_mapping.get(asset_type, "Units"))

    def add_asset(self):
        asset_type = self.cb_Asset_Types.currentText()
        name = self.cb_Asset_Name.currentText()
        subcategory = self.cb_Sub_Category_Selection.currentText()
        quantity = self.sb_Quantitative_Category.value()
        quantity_type = self.l_Quantitative_Category.text()

        if not name:
            self.log_status("Asset name is required.")
            return

        row = [
            QStandardItem(asset_type),
            QStandardItem(name),
            QStandardItem(subcategory),
            QStandardItem(str(quantity)),
            QStandardItem(quantity_type),
            QStandardItem(""),
        ]
        self.asset_model.appendRow(row)
        self.save_data_to_csv()
        self.log_status(f"Added asset: {name}")

    def remove_asset(self):
        name = self.cb_Asset_Name.currentText()
        for row_index in range(self.asset_model.rowCount()):
            if self.asset_model.item(row_index, 1).text() == name:
                self.asset_model.removeRow(row_index)
                self.save_data_to_csv()
                self.log_status(f"Removed asset: {name}")
                return

        self.log_status(f"Asset not found: {name}")

    def save_data_to_csv(self):
        rows = []
        for row_index in range(self.asset_model.rowCount()):
            rows.append({
                "Type": self.asset_model.item(row_index, 0).text(),
                "Name": self.asset_model.item(row_index, 1).text(),
                "Subcategory": self.asset_model.item(row_index, 2).text(),
                "Quantity": self.asset_model.item(row_index, 3).text(),
                "Quantity Type": self.asset_model.item(row_index, 4).text(),
                "Price": self.asset_model.item(row_index, 5).text(),
            })
        pd.DataFrame(rows).to_csv(self.asset_file, index=False)

    def refresh_graph(self):
        """Refresh the graph using historical price data."""
        try:
            if not os.path.exists(self.historical_prices_file):
                self.l_Status.setText("No historical prices data available.")
                return

            # Load the historical prices data
            with open(self.historical_prices_file, "r") as file:
                data = json.load(file)

            self.figure.clear()
            ax = self.figure.add_subplot(111)

            asset_prices = {}
            colors = {}

            # Process data and prepare for plotting
            for record in data:
                timestamp = record.get("timestamp")
                prices = record.get("prices", {})
                for asset_name, asset_data in prices.items():
                    if asset_name not in asset_prices:
                        asset_prices[asset_name] = {"timestamps": [], "prices": []}
                    asset_prices[asset_name]["timestamps"].append(timestamp)
                    asset_prices[asset_name]["prices"].append(asset_data["price"])

            # Plot each asset's data
            for i, (asset, values) in enumerate(asset_prices.items()):
                color = plt.cm.tab10(i % 10)  # Assign a unique color for each asset
                colors[asset] = to_hex(color)  # Convert to HEX for consistent legend colors
                ax.plot(
                    values["timestamps"],
                    values["prices"],
                    label=asset,
                    color=colors[asset],
                    marker="o",
                    linewidth=2
                )

            # Customizing the graph
            ax.set_title("Historical Prices of Portfolio Assets", fontsize=10)
            ax.set_xlabel("Timestamp", fontsize=5)
            ax.set_ylabel("Price (in USD)", fontsize=5)
            ax.tick_params(axis="x", rotation=15, labelsize=5)
            ax.tick_params(axis="y", labelsize=5)
            ax.grid(True, linestyle="--", alpha=0.7)

            self.canvas.draw()
            self.l_Status.setText("Graph refreshed successfully.")
            self.log_status("Graph refreshed successfully.")

            # Show the legend dialog with colors populated
            if colors:
                # self.show_legend_dialog(colors)
                self.legend_dialog = LegendDialog(self, colors)
                self.legend_dialog.show()
            else:
                self.l_Status.setText("No data for the legend dialog.")
                self.log_status("No data for the legend dialog.")

        except Exception as e:
            self.l_Status.setText(f"Failed to refresh graph: {e}")
            self.log_status(f"Failed to refresh graph: {e}")


    def show_legend_dialog(self, colors):
        """Show the legend dialog box."""
        try:
            # Create and show the legend dialog
            self.legend_dialog = LegendDialog(self, colors)
            self.legend_dialog.show()
            
        except Exception as e:
            self.log_status(f"Failed to display legend dialog: {e}")


    def display_insights(self):
        """Extract and display insights in the Insights section."""
        try:
            if not os.path.exists(self.insights_file):
                self.l_Status.setText("No insights data available.")
                return

            with open(self.insights_file, "r", encoding="utf-8") as file:
                insights_data = file.read()

            # Split and simplify insights data
            insights = insights_data.split("\n\n")
            simplified_insights = []

            for asset_data in insights:
                lines = asset_data.split("\n")
                if not lines or len(lines) < 2:
                    continue

                asset_name = lines[0].strip()
                comparisons_section = [
                    line for line in lines if line.startswith("  comparisons:")
                ]

                if comparisons_section:
                    comparisons_text = comparisons_section[0].split("comparisons:")[1].strip()
                    try:
                        # Parse comparisons into a list
                        comparisons = eval(comparisons_text)
                        simplified_insights.append(f"{asset_name}:")

                        for comp in comparisons[:5]:  # Limit to first 5 items
                            company = comp.get("Company", "Unknown")
                            price = comp.get("Price", "N/A")
                            change = comp.get("Price Change %", "N/A")
                            movement = comp.get("Movement", "N/A")
                            movement_indicator = "⬆️" if movement == "Up" else "⬇️"
                            simplified_insights.append(
                                f"- {company}: ${price}, Change: {change:.2f}%, {movement_indicator}"
                            )

                        simplified_insights.append("")  # Blank line between assets
                    except Exception as e:
                        self.log_status(f"Error parsing comparisons for {asset_name}: {e}")

            # Display insights in the scrollable area
            insights_text = "\n".join(simplified_insights)
            self.sa_Insights.setWidget(qtw.QLabel(insights_text))
            self.l_Status.setText("Insights loaded successfully.")
            self.log_status("Insights loaded successfully.")

        except Exception as e:
            self.l_Status.setText(f"Failed to load insights: {e}")
            self.log_status(f"Failed to load insights: {e}")


    def extract_portfolio(self):
        """Generate a high-quality PDF report for the portfolio."""
        try:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Title
            pdf.cell(200, 10, txt="Investment Portfolio Report", ln=True, align="C")
            pdf.ln(10)

            # Table Header
            pdf.set_font("Arial", style="B", size=10)
            pdf.cell(30, 10, txt="Type", border=1, align="C")
            pdf.cell(40, 10, txt="Name", border=1, align="C")
            pdf.cell(40, 10, txt="Subcategory", border=1, align="C")
            pdf.cell(25, 10, txt="Quantity", border=1, align="C")
            pdf.cell(30, 10, txt="Qty Type", border=1, align="C")
            pdf.cell(30, 10, txt="Price", border=1, align="C")
            pdf.ln()

            # Table Content
            pdf.set_font("Arial", size=10)
            for row_index in range(self.asset_model.rowCount()):
                pdf.cell(30, 10, txt=self.asset_model.item(row_index, 0).text(), border=1, align="C")
                pdf.cell(40, 10, txt=self.asset_model.item(row_index, 1).text(), border=1, align="C")
                pdf.cell(40, 10, txt=self.asset_model.item(row_index, 2).text(), border=1, align="C")
                pdf.cell(25, 10, txt=self.asset_model.item(row_index, 3).text(), border=1, align="C")
                pdf.cell(30, 10, txt=self.asset_model.item(row_index, 4).text(), border=1, align="C")
                price_item = self.asset_model.item(row_index, 5)
                pdf.cell(30, 10, txt=price_item.text() if price_item else "N/A", border=1, align="C")
                pdf.ln()

            # Add Graph Page
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Historical Prices Graph", ln=True, align="C")
            pdf.ln(10)

            # Save the graph with high resolution to a temporary file
            graph_image_path = self.assets_directory / "temp_historical_prices_graph.png"
            self.figure.savefig(graph_image_path, dpi=300)  # High-resolution graph

            # Add the graph image to the PDF
            pdf.image(str(graph_image_path), x=10, y=30, w=190)

            # Save the PDF to the designated PDF directory
            pdf_file = self.pdf_directory / "Portfolio_Report.pdf"
            pdf.output(str(pdf_file))

            # Clean up the temporary graph image file
            if graph_image_path.exists():
                graph_image_path.unlink()

            self.l_Status.setText(f"Portfolio saved to {pdf_file}")
            self.log_status(f"Portfolio extracted to PDF: {pdf_file}")

        except Exception as e:
            self.l_Status.setText(f"Failed to extract portfolio: {e}")
            self.log_status(f"Failed to extract portfolio: {e}")
        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = InvestmentPortfolioApp()
    window.show()
    sys.exit(app.exec())

