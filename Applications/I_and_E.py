import os
import sys
import csv
import logging
from datetime import datetime
from pathlib import Path
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from fpdf import FPDF
from windows_ui.Income_and_expense_tracker import Ui_IncomeAndExpenseTracker


class IncomeAndExpenseTrackerApp(qtw.QMainWindow, Ui_IncomeAndExpenseTracker):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._connect_signals()

        # Directory Setup
        base_directory = Path(__file__).resolve().parent
        self.data_directory = base_directory / "data storage"
        self.logs_directory = base_directory / "logs"
        self.pdf_directory = self.data_directory / "pdf"

        os.makedirs(self.data_directory, exist_ok=True)
        os.makedirs(self.logs_directory, exist_ok=True)
        os.makedirs(self.pdf_directory, exist_ok=True)

        # Logging Setup
        logging.basicConfig(
            filename=self.logs_directory / "tracker.log",
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        logging.info("Application started.")

        # Data and Metrics Initialization
        self.data = []
        self.csv_file = None
        self.total_income = 0
        self.total_budget = 0
        self.total_expenditure = 0
        self.debt = 0
        self.net_income = 0
        self.budget_surplus = 0
        self.savings_rate = 0.0
        self.emergency_funds = 0.0

        # Load the last CSV file if it exists
        self._load_last_csv()

    def _connect_signals(self):
        """Connect signals to respective slots."""
        self.pb_Income.clicked.connect(self.add_income)
        self.pb_Budget.clicked.connect(self.add_budget)
        self.pb_Expense.clicked.connect(self.add_expenditure)
        self.pb_Extract.clicked.connect(self.extract_data)

    def _update_status(self, message):
        """Update the status label with the given message."""
        self.l_Status.setText(message)
        logging.info(message)

    def _load_last_csv(self):
        """Load the last updated CSV file if it exists."""
        try:
            csv_files = [
                file for file in self.data_directory.iterdir() if file.suffix == ".csv"
            ]
            if csv_files:
                latest_file = max(csv_files, key=lambda x: x.stat().st_mtime)
                self.csv_file = latest_file
                self._load_csv_data(self.csv_file)
                self._update_status(f"Loaded data from {self.csv_file}.")
            else:
                self._update_status("No previous data to load.")
        except Exception as e:
            logging.error(f"Failed to load last CSV file: {e}")
            self._update_status("Error loading last data.")

    def _load_csv_data(self, filepath):
        """Load data from the specified CSV file."""
        self.data = []
        self.tw_Summary.setRowCount(0)  # Clear the table first
        self.total_income = 0  # Reset total income when loading new data
        try:
            with filepath.open("r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    entry_type = row["Type"]
                    budget = float(row["Budget"])
                    category = row["Category"]
                    expenditure = float(row["Expenditure"])
                    net = float(row["Net"])

                    # Add income directly to total_income and metrics
                    if entry_type == "Income":
                        self.total_income += budget

                    # Append to data and update table
                    self.data.append({
                        "Type": entry_type,
                        "Budget": budget,
                        "Category": category,
                        "Expenditure": expenditure,
                        "Net": net
                    })
                    self._update_summary_table(entry_type, budget, category, expenditure, net)

            self._update_totals()  # Recalculate all metrics
        except Exception as e:
            logging.error(f"Failed to load CSV file: {e}")
            self._update_status("Failed to load data.")

    def _update_summary_table(self, entry_type, budget, category, expenditure, net):
        """Update the summary table with a new row."""
        row_position = self.tw_Summary.rowCount()
        self.tw_Summary.insertRow(row_position)
        self.tw_Summary.setItem(row_position, 0, qtw.QTableWidgetItem(entry_type))
        self.tw_Summary.setItem(row_position, 1, qtw.QTableWidgetItem(category))
        self.tw_Summary.setItem(row_position, 2, qtw.QTableWidgetItem(f"{budget:.2f}"))
        self.tw_Summary.setItem(row_position, 3, qtw.QTableWidgetItem(f"{expenditure:.2f}"))
        self.tw_Summary.setItem(row_position, 4, qtw.QTableWidgetItem(f"{net:.2f}"))

    def _save_to_csv(self):
        """Save the current session's data to a new CSV file."""
        if not self.csv_file:
            self.csv_file = self.data_directory / f"income_expense_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        try:
            with self.csv_file.open("w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=["Type", "Budget", "Category", "Expenditure", "Net"])
                writer.writeheader()
                
                # Write only the current session data
                for entry in self.data:
                    writer.writerow(entry)
                
            logging.info(f"Data saved to {self.csv_file}.")
            self._update_status(f"Data saved to {self.csv_file}.")
        except Exception as e:
            logging.error(f"Failed to save CSV file: {e}")
            self._update_status("Failed to save data.")

    @qtc.Slot()
    def add_income(self):
        """Add income to the tracker and start a new session with a fresh CSV file."""
        try:
            income = float(self.le_Income.text())
            if income < 0:
                raise ValueError("Income cannot be negative.")

            # Reset data and UI
            self.data = []  # Clear all previous data
            self.tw_Summary.setRowCount(0)  # Clear the table
            self.total_income = income  # Set the new income
            self.total_budget = 0
            self.total_expenditure = 0
            self.debt = 0
            self.net_income = 0
            self.budget_surplus = 0
            self.savings_rate = 0.0
            self.emergency_funds = 0.0

            # Create a new CSV file
            self.csv_file = self.data_directory / f"income_expense_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

            # Add the new income entry to data and table
            income_entry = {
                "Type": "Income",
                "Budget": income,
                "Category": "Income",
                "Expenditure": 0.0,
                "Net": income
            }
            self.data.append(income_entry)  # Add to data
            self._update_summary_table("Income", income, "Income", 0.0, income)  # Update table

            # Save the new data to the new CSV file
            self._save_to_csv()

            # Update the status
            self._update_status("New income added successfully. Session reset.")
        except ValueError:
            qtw.QMessageBox.warning(self, "Invalid Input", "Please enter a valid income amount.")
            self._update_status("Failed to add income: Invalid input.")
        finally:
            self.le_Income.clear()

    @qtc.Slot()
    def add_budget(self):
        """Add a budget for a specific category."""
        try:
            budget = float(self.sb_Budget.value())
            category = self.cb_Budget_Category.currentText()
            if budget < 0:
                raise ValueError("Budget cannot be negative.")

            self.data.append({"Type": "Budget", "Budget": budget, "Category": category, "Expenditure": 0.0, "Net": budget})
            self._update_summary_table("Budget", budget, category, 0.0, budget)
            self._update_totals()
            self._save_to_csv()
            self._update_status(f"Budget for '{category}' added successfully.")
        except ValueError:
            qtw.QMessageBox.warning(self, "Invalid Input", "Please enter a valid budget amount.")
            self._update_status("Failed to add budget: Invalid input.")

    @qtc.Slot()
    def add_expenditure(self):
        """Add an expenditure for a specific category."""
        try:
            expenditure = float(self.sb_Expense.value())
            category = self.cb_Expense_Category.currentText()
            if expenditure < 0:
                raise ValueError("Expenditure cannot be negative.")

            # Find and update the corresponding budget entry
            updated = False
            for entry in self.data:
                if entry["Category"] == category and entry["Type"] == "Budget":
                    entry["Expenditure"] += expenditure
                    entry["Net"] -= expenditure
                    updated = True

            if not updated:
                self.data.append({"Type": "Expenditure", "Budget": 0.0, "Category": category, "Expenditure": expenditure, "Net": -expenditure})

            self._update_summary_table("Expenditure", 0.0, category, expenditure, -expenditure)
            self._update_totals()
            self._save_to_csv()
            self._update_status(f"Expenditure for '{category}' added successfully.")
        except ValueError:
            qtw.QMessageBox.warning(self, "Invalid Input", "Please enter a valid expenditure amount.")
            self._update_status("Failed to add expenditure: Invalid input.")

    def _update_totals(self):
        """Update all totals and calculated metrics."""
        self.total_budget = sum(float(row["Budget"]) for row in self.data if row["Type"] == "Budget")
        self.total_expenditure = sum(float(row["Expenditure"]) for row in self.data)
        self.debt = (self.total_expenditure - self.total_budget) if self.total_expenditure > self.total_budget else 0
        self.net_income = self.total_income - self.debt
        self.budget_surplus = (self.total_budget - self.total_expenditure) if self.total_expenditure > 0 else 0
        self.emergency_funds = self.net_income * 0.1
        self.savings_rate = ((self.net_income - self.total_expenditure - self.emergency_funds) / self.total_income * 100) if self.net_income > 0 else 0

        # Update UI
        self.l_Total_Income.setText(f"Total Income: ₹{self.total_income:.2f}")
        self.l_Total_Budget.setText(f"Total Budget: ₹{self.total_budget:.2f}")
        self.l_Total_Expenses.setText(f"Total Expenditure: ₹{self.total_expenditure:.2f}")
        self.l_Debt.setText(f"Debt: ₹{self.debt:.2f}")
        self.l_Net_Income.setText(f"Net Income: ₹{self.net_income:.2f}")
        self.l_Budget_Surplus.setText(f"Budget Surplus: ₹{self.budget_surplus:.2f}")
        self.l_Savings_Rate.setText(f"Savings Rate: {self.savings_rate:.2f}%")
        self.l_Emergency_Funds.setText(f"Emergency Funds: ₹{self.emergency_funds:.2f}")

        logging.info("Metrics updated.")

    def extract_data(self):
        """Extract data and metrics to a PDF file."""
        try:
            pdf_file = self.pdf_directory / f"{self.csv_file.stem}.pdf"

            # Create PDF
            pdf = FPDF()
            pdf.add_page()

            # Add Times New Roman font (ensure the font is available)
            pdf.add_font('Times', '', str(Path(os.environ.get('WINDIR', 'C:/Windows')) / 'Fonts/times.ttf'), uni=True)
            pdf.set_font("Times", size=12)  # Use Times New Roman with size 12

            # Add Title
            pdf.cell(200, 10, txt="Income and Expense Tracker", ln=True, align="C")
            pdf.ln(10)

            # Add Table Header
            pdf.set_font("Times", style="B", size=12)
            pdf.cell(40, 10, "Type", 1, 0, "C")
            pdf.cell(50, 10, "Category", 1, 0, "C")
            pdf.cell(40, 10, "Budget", 1, 0, "C")
            pdf.cell(40, 10, "Expenditure", 1, 0, "C")
            pdf.cell(40, 10, "Net", 1, 1, "C")

            # Add Table Data
            pdf.set_font("Times", size=12)
            for row in self.data:
                pdf.cell(40, 10, row["Type"], 1, 0, "C")
                pdf.cell(50, 10, row["Category"], 1, 0, "C")
                pdf.cell(40, 10, f"{float(row['Budget']):.2f}", 1, 0, "C")
                pdf.cell(40, 10, f"{float(row['Expenditure']):.2f}", 1, 0, "C")
                pdf.cell(40, 10, f"{float(row['Net']):.2f}", 1, 1, "C")

            # Add Metrics Below Table
            pdf.ln(10)
            pdf.set_font("Times", style="B", size=12)
            pdf.cell(200, 10, txt="Calculated Metrics", ln=True, align="L")
            pdf.set_font("Times", size=12)
            pdf.cell(200, 10, txt=f"Total Income: Rupees {self.total_income:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Total Budget: Rupees {self.total_budget:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Total Expenditure: Rupees {self.total_expenditure:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Debt: Rupees {self.debt:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Net Income: Rupees {self.net_income:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Budget Surplus: Rupees {self.budget_surplus:.2f}", ln=True)
            pdf.cell(200, 10, txt=f"Savings Rate: {self.savings_rate:.2f}%", ln=True)
            pdf.cell(200, 10, txt=f"Emergency Funds: Rupees {self.emergency_funds:.2f}", ln=True)

            pdf.output(str(pdf_file))

            logging.info(f"Data extracted to {pdf_file}.")
            self._update_status("Data extracted successfully.")
        except Exception as e:
            logging.error(f"Failed to extract data: {e}")
            self._update_status(f"Failed to extract data: {e}")


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    window = IncomeAndExpenseTrackerApp()
    window.show()
    sys.exit(app.exec())
