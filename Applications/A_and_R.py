import os
import sys
import logging
import csv
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QMessageBox
from PySide6 import QtCore as qtc
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import pandas as pd
from fpdf import FPDF
from pathlib import Path
from windows_ui.Analytics_and_Recommendations import Ui_Analytics_and_Recommendations


class AnalyticsAndRecommendationsApp(QMainWindow, Ui_Analytics_and_Recommendations):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._connect_signals()

        base_directory = Path(__file__).resolve().parent
        self.data_directory = base_directory / "data storage"
        self.logs_directory = base_directory / "logs"
        self.pdf_directory = self.data_directory / "pdf"
        self.data = None  # Placeholder for loaded data

        self.data_directory.mkdir(parents=True, exist_ok=True)
        self.logs_directory.mkdir(parents=True, exist_ok=True)
        self.pdf_directory.mkdir(parents=True, exist_ok=True)

        # Logging Setup
        logging.basicConfig(
            filename=self.logs_directory / "analytics.log",
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logging.info("Analytics and Recommendations App Initialized.")
        self.load_data()

        # Initialize graphs
        self.line_graph_canvas = None
        self.pie_chart_canvas = None
        self._setup_graphs()

        # Display initial insights
        self._display_insights()

    def _connect_signals(self):
        """Connect UI signals to their respective slots."""
        self.pb_Projection.clicked.connect(self.generate_predictions)
        self.pb_Past_Data_Visualize.clicked.connect(self.visualize_past_data)
        self.pb_Export_Analytics.clicked.connect(self.export_analytics)
        self.pb_Export_Predictions.clicked.connect(self.export_predictions)

    def _setup_graphs(self):
        """Set up placeholders for line graph and pie chart."""
        # Line graph
        self.line_graph_canvas = FigureCanvas(plt.figure())
        if not self.f_Line_Graph.layout():
            line_graph_layout = QVBoxLayout(self.f_Line_Graph)
            self.f_Line_Graph.setLayout(line_graph_layout)
        line_graph_layout = self.f_Line_Graph.layout()
        line_graph_layout.addWidget(self.line_graph_canvas)

        # Pie chart
        self.pie_chart_canvas = FigureCanvas(plt.figure())
        if not self.f_Pie_Graph.layout():
            pie_chart_layout = QVBoxLayout(self.f_Pie_Graph)
            self.f_Pie_Graph.setLayout(pie_chart_layout)
        pie_chart_layout = self.f_Pie_Graph.layout()
        pie_chart_layout.addWidget(self.pie_chart_canvas)

    def load_data(self):
        """Load and aggregate past expense data from CSV files."""
        try:
            csv_files = [file for file in self.data_directory.glob("*.csv")]

            if not csv_files:
                self.l_Status.setText("No CSV files found in the data directory.")
                logging.warning("No CSV files found in the data directory.")
                return

            all_data = []
            for file in csv_files:
                try:
                    df = pd.read_csv(file)
                    all_data.append(df)
                    logging.info(f"Loaded data from {file}.")
                except Exception as e:
                    logging.error(f"Failed to load {file}: {e}")
                    self.l_Status.setText(f"Error loading {file}: {e}")

            if all_data:
                self.data = pd.concat(all_data, ignore_index=True)
                self.l_Status.setText("Data loaded successfully.")
                logging.info("Data loaded successfully.")
            else:
                self.l_Status.setText("No valid data to load.")
                logging.warning("No valid data to load.")
        except Exception as e:
            self.l_Status.setText(f"Error loading data: {e}")
            logging.error(f"Error loading data: {e}")

    def _generate_insights(self):
        """Generate dynamic insights from all the data loaded from all CSV files."""
        if self.data is None or self.data.empty:
            logging.warning("No data available to generate insights.")
            return []

        insights = []
        try:
            # Aggregated totals
            total_budget = self.data[self.data["Type"] == "Budget"]["Budget"].sum()
            total_expenditure = self.data["Expenditure"].sum()
            total_income = self.data[self.data["Type"] == "Income"]["Net"].sum()
            emergency_funds = total_income * 0.1  # 10% of income as emergency funds

            # Total Expenditure vs. Total Budget
            if total_budget > total_expenditure:
                insights.append(
                    f"Overall: Your total expenditure ({total_expenditure:.2f}) is within the budget ({total_budget:.2f})."
                )
            else:
                insights.append(
                    f"Overall: Your total expenditure ({total_expenditure:.2f}) exceeds the budget ({total_budget:.2f})."
                )

            # Savings Rate Insights
            if total_income > 0:
                savings_rate = (
                    ((total_income - total_expenditure - emergency_funds) / total_income) * 100
                )
                if savings_rate > 20:
                    insights.append(
                        f"Overall: You have a healthy savings rate of {savings_rate:.2f}%. Keep it up!"
                    )
                else:
                    insights.append(
                        f"Overall: Your savings rate is {savings_rate:.2f}%. Consider reviewing your expenditures."
                    )
            else:
                insights.append("Overall: No income data available to calculate savings rate.")

            # Largest Expenditure Category
            category_totals = self.data.groupby("Category")["Expenditure"].sum()
            if not category_totals.empty:
                largest_category = category_totals.idxmax()
                largest_category_amount = category_totals.max()
                insights.append(
                    f"Overall: The largest expenditure category is '{largest_category}' with a total of {largest_category_amount:.2f}."
                )

            # Monthly Trends
            monthly_totals = self.data.groupby("Month")["Expenditure"].sum()
            if len(monthly_totals) > 1:
                expenditure_trend = "increasing" if monthly_totals.diff().mean() > 0 else "decreasing"
                insights.append(
                    f"Overall: Your monthly expenditures are generally {expenditure_trend} over time."
                )

            # Recent Monthly Insights (Last Month Only)
            recent_data = self.data[self.data["Month"] == self.data["Month"].max()]
            recent_month = self.data["Month"].max()

            recent_budget = recent_data[recent_data["Type"] == "Budget"]["Budget"].sum()
            recent_expenditure = recent_data["Expenditure"].sum()
            recent_income = recent_data[recent_data["Type"] == "Income"]["Net"].sum()
            recent_emergency_funds = recent_income * 0.1

            if recent_budget > recent_expenditure:
                insights.append(
                    f"Last Month ({recent_month}): Your expenditure ({recent_expenditure:.2f}) was within the budget ({recent_budget:.2f})."
                )
            else:
                insights.append(
                    f"Last Month ({recent_month}): Your expenditure ({recent_expenditure:.2f}) exceeded the budget ({recent_budget:.2f})."
                )

            if recent_income > 0:
                recent_savings_rate = (
                    ((recent_income - recent_expenditure - recent_emergency_funds) / recent_income) * 100
                )
                if recent_savings_rate > 20:
                    insights.append(
                        f"Last Month ({recent_month}): You had a healthy savings rate of {recent_savings_rate:.2f}%. Great job!"
                    )
                else:
                    insights.append(
                        f"Last Month ({recent_month}): Your savings rate was {recent_savings_rate:.2f}%. Consider reducing expenses."
                    )
            else:
                insights.append(f"Last Month ({recent_month}): No income data available to calculate savings rate.")

            # Recent Monthly Largest Category
            recent_category_totals = recent_data.groupby("Category")["Expenditure"].sum()
            if not recent_category_totals.empty:
                recent_largest_category = recent_category_totals.idxmax()
                recent_largest_category_amount = recent_category_totals.max()
                insights.append(
                    f"Last Month ({recent_month}): The largest expenditure category was '{recent_largest_category}' with a total of {recent_largest_category_amount:.2f}."
                )

        except Exception as e:
            logging.error(f"Error generating insights: {e}")

        logging.info(f"Generated insights: {insights}")
        return insights

    def _display_insights(self):
        """Display insights dynamically in the Insights section."""
        insights = self._generate_insights()
        if not insights:
            self._display_message(self.f_Insights, "No insights available.")
            return

        # Display insights in the scrollable area
        layout = QVBoxLayout()
        for insight in insights:
            label = QLabel(insight)
            label.setWordWrap(True)
            layout.addWidget(label)

        # Clear and set new layout
        if self.gb_Insights.layout():
            for i in reversed(range(self.f_Insights.layout().count())):
                self.f_Insights.layout().itemAt(i).widget().setParent(None)
            self.f_Insights.layout().deleteLater()
        self.gb_Insights.setLayout(layout)
    
    @qtc.Slot()
    def visualize_past_data(self):
        """Visualize past data with line and pie charts."""
        if self.data is None or self.data.empty:
            QMessageBox.warning(self, "No Data", "No data available for analysis. Please load valid data.")
            self.l_Status.setText("No data available. Load data first.")
            logging.warning("No data available for analysis.")
            return

        try:
            # Visualize line graph
            self._visualize_line_graph()

            # Visualize pie chart
            self._visualize_pie_chart()

            self.l_Status.setText("Past data visualized successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error visualizing data: {e}")
            self.l_Status.setText(f"Error visualizing data: {e}")
            logging.error(f"Error visualizing data: {e}")

    def _visualize_line_graph(self):
        """Helper method to visualize the line graph."""
        total_budgets = []
        total_expenses = []
        savings_rates = []
        ideal_expenses = []
        file_dates = []

        csv_files = sorted(
            [
                file for file in self.data_directory.glob("*.csv")
            ],
            key=os.path.getmtime,
        )

        for file in csv_files:
            try:
                df = pd.read_csv(file)
                total_budget = df[df["Type"] == "Budget"]["Budget"].sum()
                total_expense = df["Expenditure"].sum()
                total_income = df[df["Type"] == "Income"]["Net"].sum()

                emergency_funds = total_income * 0.1
                savings_rate = (
                    ((total_income - total_expense - emergency_funds) / total_income) * 100
                    if total_income > 0
                    else 0
                )
                ideal_expenditure = (total_income / 2) - emergency_funds

                total_budgets.append(total_budget)
                total_expenses.append(total_expense)
                savings_rates.append(savings_rate)
                ideal_expenses.append(ideal_expenditure)
                file_dates.append(os.path.basename(file).split("_")[2])
            except Exception as e:
                logging.error(f"Failed to process {file}: {e}")
                continue

        self._plot_analysis_data(file_dates, total_budgets, total_expenses, ideal_expenses, savings_rates)

    def _visualize_pie_chart(self):
        """Helper method to visualize the pie chart."""
        try:
            # Calculate mean expenditure by category
            category_means = self.data.groupby("Category")["Expenditure"].mean()
            filtered_means = category_means[category_means > 0]

            if filtered_means.empty:
                QMessageBox.warning(self, "No Valid Data", "No valid data for creating a pie chart.")
                self.l_Status.setText("No valid data found for pie chart.")
                return

            percentages = (filtered_means / filtered_means.sum()) * 100

            self.pie_chart_canvas.figure.clear()
            ax = self.pie_chart_canvas.figure.add_subplot(111)
            wedges, texts, autotexts = ax.pie(
                filtered_means.values,
                labels=filtered_means.index,
                autopct=lambda p: f'{p:.1f}%' if p > 0 else '',
                startangle=140
            )
            # Set title in one line with a smaller font size
            ax.set_title("Mean Expenditure Distribution by Category", fontsize=5)

            # Style the text for better visibility
            for text in texts + autotexts:
                text.set_fontsize(5)

            self.pie_chart_canvas.draw()

            # Prepare legend for pie chart
            pie_chart_legend = {
                category: f"{percentage:.1f}%" for category, percentage in zip(filtered_means.index, percentages)
            }

            # Show combined legend dialog
            line_graph_legend = {
                "Total Budget": "blue, solid line with circle markers",
                "Total Expenses": "red, solid line with circle markers",
                "Ideal Total Expenses": "green, dashed line",
                "Savings Rate (%)": "purple, dotted line with cross markers",
            }
            self._show_combined_legend_dialog(line_graph_legend, pie_chart_legend)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error visualizing pie chart: {e}")
            logging.error(f"Error visualizing pie chart: {e}")

    def _show_combined_legend_dialog(self, line_graph_legend, pie_chart_legend):
        """Display a combined legend dialog with legends for both line and pie charts."""
        legend_text = "Legend for the graphs:\n\n"

        # Add Line Graph Legend
        legend_text += "Line Graph:\n"
        for key, value in line_graph_legend.items():
            legend_text += f"  {key}: {value}\n"

            # Add Pie Chart Legend
        legend_text += "\nPie Chart:\n"
        for key, value in pie_chart_legend.items():
            legend_text += f"  {key}: {value}\n"

        QMessageBox.information(self, "Combined Graph Legend", legend_text)

    def _plot_analysis_data(self, file_dates, total_budgets, total_expenses, ideal_expenses, savings_rates):
        """Helper method to plot analysis data."""
        self.line_graph_canvas.figure.clear()
        ax1 = self.line_graph_canvas.figure.add_subplot(111)

        # Plot total budgets and expenses
        ax1.plot(file_dates, total_budgets, color="blue", marker="o", label="Total Budget")
        ax1.plot(file_dates, total_expenses, color="red", marker="o", label="Total Expenses")
        ax1.plot(file_dates, ideal_expenses, color="green", linestyle="--", marker="o", label="Ideal Total Expenses")
        ax1.set_xlabel("File Dates", fontsize=8)
        ax1.set_ylabel("Amount", fontsize=8)
        ax1.set_title("Budget, Expenses, and Ideal Expenditures", fontsize=10)

        # Adjust font sizes for x-ticks and y-ticks for better visibility
        ax1.tick_params(axis='x', labelsize=6)
        ax1.tick_params(axis='y', labelsize=6)

        # Plot savings rates on a secondary axis
        ax2 = ax1.twinx()
        ax2.plot(file_dates, savings_rates, color="purple", linestyle=":", marker="x", label="Savings Rate (%)")
        ax2.set_ylabel("Savings Rate (%)", fontsize=8)
        ax2.tick_params(axis='y', labelsize=6)

        # Tighten the layout for better fitting within the frame
        self.line_graph_canvas.figure.tight_layout()
        self.line_graph_canvas.draw()

    @qtc.Slot()
    def export_predictions(self):
        """Export predictions (graphs and insights) to a high-quality PDF file."""
        try:
            # Ensure directories exist
            self.data_directory.mkdir(parents=True, exist_ok=True)
            self.pdf_directory.mkdir(parents=True, exist_ok=True)

            # Initialize PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add title
            pdf.cell(200, 10, txt="Expense Predictions Report", ln=True, align="C")
            pdf.ln(10)

            # Generate and add predictions
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt="Predictions:", ln=True)
            predictions = self._generate_predictions_text()  # Dynamically generate predictions
            if predictions:
                for prediction in predictions:
                    pdf.multi_cell(0, 10, f"- {prediction}")  # Use multi-cell for proper formatting
            else:
                pdf.cell(200, 10, txt="No predictions available.", ln=True)
            pdf.ln(10)

            # Save Predictions Graph
            line_graph_path = self.data_directory / "line_graph.png"
            try:
                self.line_graph_canvas.figure.tight_layout()
                self.line_graph_canvas.figure.savefig(line_graph_path, dpi=300)
                pdf.cell(200, 10, txt="Predictions Graph:", ln=True)
                pdf.ln(10)
                pdf.image(str(line_graph_path), x=10, y=None, w=180)
            except Exception as e:
                logging.error(f"Error saving line graph: {e}")
                self.l_Status.setText(f"Error saving line graph: {e}")
                return

            # Save Predicted Pie Chart (if available)
            if hasattr(self, 'pie_chart_canvas'):
                pie_chart_path = self.data_directory / "pie_chart.png"
                try:
                    self.pie_chart_canvas.figure.tight_layout()
                    self.pie_chart_canvas.figure.savefig(pie_chart_path, dpi=300)
                    pdf.add_page()
                    pdf.cell(200, 10, txt="Predicted Expenditure Distribution Pie Chart:", ln=True)
                    pdf.ln(10)
                    pdf.image(str(pie_chart_path), x=10, y=None, w=180)
                except Exception as e:
                    logging.error(f"Error saving pie chart: {e}")
                    self.l_Status.setText(f"Error saving pie chart: {e}")
                    return

            # Save the PDF
            pdf_path = self.pdf_directory / "Expense_Predictions_Report.pdf"
            try:
                pdf.output(str(pdf_path))
                self.l_Status.setText(f"Predictions exported to {pdf_path}.")
                logging.info(f"Predictions exported to {pdf_path}.")
            except Exception as e:
                logging.error(f"Error saving PDF: {e}")
                self.l_Status.setText(f"Error saving PDF: {e}")
                return

            # Clean up temporary image files
            try:
                if line_graph_path.exists():
                    line_graph_path.unlink()
                if 'pie_chart_path' in locals() and pie_chart_path.exists():
                    pie_chart_path.unlink()
            except Exception as e:
                logging.error(f"Error during file cleanup: {e}")
                self.l_Status.setText(f"Error during file cleanup: {e}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error exporting predictions: {e}")
            self.l_Status.setText(f"Error exporting predictions: {e}")
            logging.error(f"Error exporting predictions: {e}")

    @qtc.Slot()
    def export_analytics(self):
        """Export analytics (graphs and insights) to a PDF file."""
        try:
            # Ensure directories exist
            self.data_directory.mkdir(parents=True, exist_ok=True)
            self.pdf_directory.mkdir(parents=True, exist_ok=True)

            # Initialize PDF
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            # Add title
            pdf.cell(200, 10, txt="Expense Analytics Report", ln=True, align="C")
            pdf.ln(10)

            # Generate and add insights
            pdf.set_font("Arial", size=10)
            pdf.cell(200, 10, txt="Insights:", ln=True)
            insights = self._generate_insights()  # Dynamically generate insights
            if insights:
                for insight in insights:
                    pdf.multi_cell(0, 10, f"- {insight}")  # Use multi-cell for proper formatting
            else:
                pdf.cell(200, 10, txt="No insights available.", ln=True)
            pdf.ln(10)

            # Save Line Graph
            line_graph_path = self.data_directory / "line_graph.png"
            try:
                self.line_graph_canvas.figure.tight_layout()
                self.line_graph_canvas.figure.savefig(line_graph_path, dpi=300)
                pdf.cell(200, 10, txt="Line Graph:", ln=True)
                pdf.ln(10)
                pdf.image(str(line_graph_path), x=10, y=None, w=180)
            except Exception as e:
                logging.error(f"Error saving line graph: {e}")
                self.l_Status.setText(f"Error saving line graph: {e}")
                return

            # Save Pie Chart (if available)
            if hasattr(self, 'pie_chart_canvas'):
                pie_chart_path = self.data_directory / "pie_chart.png"
                try:
                    self.pie_chart_canvas.figure.tight_layout()
                    self.pie_chart_canvas.figure.savefig(pie_chart_path, dpi=300)
                    pdf.add_page()
                    pdf.cell(200, 10, txt="Pie Chart:", ln=True)
                    pdf.ln(10)
                    pdf.image(str(pie_chart_path), x=10, y=None, w=180)
                except Exception as e:
                    logging.error(f"Error saving pie chart: {e}")
                    self.l_Status.setText(f"Error saving pie chart: {e}")
                    return

            # Save the PDF
            pdf_path = self.pdf_directory / "Expense_Analytics_Report.pdf"
            try:
                pdf.output(str(pdf_path))
                self.l_Status.setText(f"Analytics exported to {pdf_path}.")
                logging.info(f"Analytics exported to {pdf_path}.")
            except Exception as e:
                logging.error(f"Error saving PDF: {e}")
                self.l_Status.setText(f"Error saving PDF: {e}")
                return

            # Clean up temporary image files
            try:
                if line_graph_path.exists():
                    line_graph_path.unlink()
                if 'pie_chart_path' in locals() and pie_chart_path.exists():
                    pie_chart_path.unlink()
            except Exception as e:
                logging.error(f"Error during file cleanup: {e}")
                self.l_Status.setText(f"Error during file cleanup: {e}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error exporting analytics: {e}")
            self.l_Status.setText(f"Error exporting analytics: {e}")
            logging.error(f"Error exporting analytics: {e}")

    @qtc.Slot()
    def generate_predictions(self):
        """Predict future data and update the graph."""
        if self.data is None or self.data.empty:
            QMessageBox.warning(self, "No Data", "No data available for predictions. Please load valid data.")
            self.l_Status.setText("No data available for predictions.")
            logging.warning("No data available for predictions.")
            return

        try:
            # Assign a chronological "Month" value to each file based on the upload order
            csv_files = sorted(
                [
                    os.path.join(self.data_directory, f)
                    for f in os.listdir(self.data_directory)
                    if f.endswith(".csv")
                ],
                key=os.path.getmtime,  # Sort by modification time
            )

            monthly_data = []
            for idx, file in enumerate(csv_files, start=1):
                df = pd.read_csv(file)
                df["Month"] = idx  # Assign chronological month value
                monthly_data.append(df)

            combined_data = pd.concat(monthly_data, ignore_index=True)

            # Group data by "Month"
            monthly_totals = combined_data.groupby("Month")["Expenditure"].sum()
            total_incomes = combined_data.groupby("Month")["Net"].sum()

            # Calculate growth rates for predictions
            if len(monthly_totals) > 1:
                expenditure_growth_rate = monthly_totals.pct_change().mean()
                income_growth_rate = total_incomes.pct_change().mean()
            else:
                expenditure_growth_rate = 0
                income_growth_rate = 0

            # Predict future total expenditures and incomes
            current_month_index = len(monthly_totals)
            future_months = [f"Month +{i}" for i in range(1, 7)]
            last_expenditure = monthly_totals.iloc[-1] if not monthly_totals.empty else 0
            last_income = total_incomes.iloc[-1] if not total_incomes.empty else 0
            future_totals = [last_expenditure * ((1 + expenditure_growth_rate) ** i) for i in range(1, 7)]
            future_incomes = [last_income * ((1 + income_growth_rate) ** i) for i in range(1, 7)]
            ideal_expenses = [(income / 2) - (income * 0.1) for income in future_incomes]

            # Predict expenditures for each category for the next month
            recent_data = combined_data[combined_data["Month"] == combined_data["Month"].max()]
            category_totals = recent_data.groupby("Category")["Expenditure"].sum()
            next_month_predictions = {
                category: value * (1 + expenditure_growth_rate)
                for category, value in category_totals.items()
                if value > 0.0
            }
            # Calculate ideal expenditure for the next month based on predicted income
            next_month_ideal_expenditure = (last_income * (1 + income_growth_rate) / 2) - (last_income * (1 + income_growth_rate) * 0.1)

            # Plot predictions for the next 6 months
            self._plot_prediction_data(
                future_months=future_months,
                predictions=future_totals,
                ideal_expenses=ideal_expenses,
            )

            # Visualize category-wise predictions as a pie chart
            self._visualize_predicted_pie_chart(next_month_predictions)

            # Display category-wise predictions and recommended ideal expenditure in the scroll area
            insights = ["Predicted expenditures for each category for the next month:"]
            insights.extend([f"  {category}: {amount:.2f}" for category, amount in next_month_predictions.items()])
            insights.append(f"Recommended Ideal Expenditure for next month: {next_month_ideal_expenditure:.2f}")
            self._display_predictions(insights)

            self.l_Status.setText("Predictions generated successfully.")
            logging.info("Predictions generated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error generating predictions: {e}")
            self.l_Status.setText(f"Error generating predictions: {e}")
            logging.error(f"Error generating predictions: {e}")

    def _generate_predictions_text(self):
        """Generate predictions text for export."""
        predictions_text = []
        try:
            # Prepare data for the predictions
            csv_files = sorted(
                [
                    os.path.join(self.data_directory, f)
                    for f in os.listdir(self.data_directory)
                    if f.endswith(".csv")
                ],
                key=os.path.getmtime,
            )

            monthly_data = []
            for idx, file in enumerate(csv_files, start=1):
                df = pd.read_csv(file)
                df["Month"] = idx  # Assign chronological month value
                monthly_data.append(df)

            combined_data = pd.concat(monthly_data, ignore_index=True)

            # Group data by "Month"
            monthly_totals = combined_data.groupby("Month")["Expenditure"].sum()
            total_incomes = combined_data.groupby("Month")["Net"].sum()

            # Calculate growth rates for predictions
            if len(monthly_totals) > 1:
                expenditure_growth_rate = monthly_totals.pct_change().mean()
                income_growth_rate = total_incomes.pct_change().mean()
            else:
                expenditure_growth_rate = 0
                income_growth_rate = 0

            # Predict future total expenditures and incomes
            last_expenditure = monthly_totals.iloc[-1] if not monthly_totals.empty else 0
            last_income = total_incomes.iloc[-1] if not total_incomes.empty else 0
            future_totals = [last_expenditure * ((1 + expenditure_growth_rate) ** i) for i in range(1, 7)]
            future_incomes = [last_income * ((1 + income_growth_rate) ** i) for i in range(1, 7)]
            ideal_expenses = [(income / 2) - (income * 0.1) for income in future_incomes]

            # Predict expenditures for each category for the next month
            recent_data = combined_data[combined_data["Month"] == combined_data["Month"].max()]
            category_totals = recent_data.groupby("Category")["Expenditure"].sum()
            next_month_predictions = {
                category: value * (1 + expenditure_growth_rate)
                for category, value in category_totals.items()
                if value > 0.0
            }
            next_month_ideal_expenditure = (last_income * (1 + income_growth_rate) / 2) - (last_income * (1 + income_growth_rate) * 0.1)

            # Add predictions to the text output
            predictions_text.append("Predicted expenditures for each category for the next month:")
            predictions_text.extend([f"  {category}: {amount:.2f}" for category, amount in next_month_predictions.items()])
            predictions_text.append(f"Recommended Ideal Expenditure for next month: {next_month_ideal_expenditure:.2f}")

            # Add future months predictions
            predictions_text.append("\nPredicted total expenditures for the next 6 months:")
            for i, total in enumerate(future_totals):
                predictions_text.append(f"  Month +{i + 1}: {total:.2f}")

            predictions_text.append("\nPredicted ideal expenditures for the next 6 months:")
            for i, ideal in enumerate(ideal_expenses):
                predictions_text.append(f"  Month +{i + 1}: {ideal:.2f}")
        except Exception as e:
            logging.error(f"Error generating predictions text: {e}")
            predictions_text.append("Error generating predictions.")

        return predictions_text

    def _visualize_predicted_pie_chart(self, predictions):
        """Visualize the predicted expenses per category as a pie chart."""
        if not predictions:
            QMessageBox.warning(self, "No Predictions", "No valid predictions available for category-wise pie chart.")
            self.l_Status.setText("No predictions available for pie chart.")
            logging.warning("No predictions available for pie chart.")
            return

        try:
            # Prepare data for the pie chart
            categories = list(predictions.keys())
            values = list(predictions.values())

            # Clear the previous pie chart
            self.pie_chart_canvas.figure.clear()
            ax = self.pie_chart_canvas.figure.add_subplot(111)

            # Create pie chart
            wedges, texts, autotexts = ax.pie(
                values,
                labels=categories,
                autopct=lambda p: f"{p:.1f}%" if p > 0 else "",
                startangle=140
            )
            ax.set_title("Predicted Expenditure Distribution by Category", fontsize=5)

            # Style text for better visibility
            for text in texts + autotexts:
                text.set_fontsize(6)

            self.pie_chart_canvas.draw()

            self.l_Status.setText("Predicted pie chart generated successfully.")
            logging.info("Predicted pie chart generated successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error visualizing predicted pie chart: {e}")
            logging.error(f"Error visualizing predicted pie chart: {e}")


    def _display_predictions(self, predictions):
        """Display predictions dynamically in the Predictions section."""
        if not predictions:
            self._display_message(self.sa_Predicted_Expenses, "No predictions available.")
            return

        # Ensure the scroll area has a widget and layout for predictions
        if not self.sa_Predicted_Expenses.widget():
            self.sa_Predicted_Expenses.setWidget(QLabel())
            self.sa_Predicted_Expenses.setWidgetResizable(True)

        # Create a layout to display predictions
        predictions_widget = self.sa_Predicted_Expenses.widget()
        layout = predictions_widget.layout()

        if layout is None:
            layout = QVBoxLayout()
            predictions_widget.setLayout(layout)

        # Clear the existing layout
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        # Add predictions to the layout
        for prediction in predictions:
            label = QLabel(prediction)
            label.setWordWrap(True)
            layout.addWidget(label)

        # Ensure the layout updates
        self.sa_Predicted_Expenses.setWidget(predictions_widget)

    def _plot_prediction_data(self, future_months, predictions, ideal_expenses):
        """Helper method to plot prediction data."""
        self.line_graph_canvas.figure.clear()
        ax1 = self.line_graph_canvas.figure.add_subplot(111)

        # Plot predicted data
        ax1.plot(future_months, predictions, color="orange", linestyle="--", marker="o", label="Predicted Total Expenditure")
        ax1.plot(future_months, ideal_expenses, color="green", linestyle="--", marker="x", label="Ideal Expenses")
        ax1.set_title("Monthly Expense Predictions", fontsize=10)
        ax1.set_xlabel("Months", fontsize=8)
        ax1.set_ylabel("Amount", fontsize=8)
        ax1.tick_params(axis="x", labelsize=6)
        ax1.tick_params(axis="y", labelsize=6)
        ax1.legend(fontsize=8)

        # Adjust layout
        self.line_graph_canvas.figure.tight_layout()
        self.line_graph_canvas.draw()

    def _display_message(self, frame, message):
        """Display a message in the given frame."""
        if frame.layout() is not None:
            for i in reversed(range(frame.layout().count())):
                frame.layout().itemAt(i).widget().setParent(None)
        label = QLabel(message)
        label.setAlignment(qtc.Qt.AlignCenter)
        frame.layout().addWidget(label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnalyticsAndRecommendationsApp()
    window.show()
    sys.exit(app.exec())

