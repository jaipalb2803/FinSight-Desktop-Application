import sys
import subprocess
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow
from windows_ui.Finsight_Dashboard import Ui_Dashboard  # Import the auto-generated UI class

# Define the root directory dynamically based on the parent of the current file
ROOT_DIR = Path(__file__).resolve().parent.parent  # Move one level up to the project root

class MainDashboard(QMainWindow, Ui_Dashboard):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Set up the UI components

        # Connect buttons to their respective slots
        self.pb_Income_Expense.clicked.connect(self.open_income_expense)
        self.pb_Analyze_Recommend.clicked.connect(self.open_analysis_recommendation)
        self.pb_Investment_Portfolio.clicked.connect(self.open_investment_portfolio)

    def open_income_expense(self):
        """Opens the Income and Expense Tracker script."""
        python_path = Path(sys.executable)  # Use the currently running Python executable
        script_path = ROOT_DIR / "Applications" / "I_and_E.py"
        try:
            subprocess.Popen([str(python_path), str(script_path)])
        except Exception as e:
            print(f"Failed to open {script_path}: {e}")

    def open_analysis_recommendation(self):
        """Opens the Analysis and Recommendation script."""
        python_path = Path(sys.executable)  # Use the currently running Python executable
        script_path = ROOT_DIR / "Applications" / "A_and_R.py"
        try:
            subprocess.Popen([str(python_path), str(script_path)])
        except Exception as e:
            print(f"Failed to open {script_path}: {e}")

    def open_investment_portfolio(self):
        """Opens the Investment Portfolio script."""
        python_path = Path(sys.executable)  # Use the currently running Python executable
        script_path = ROOT_DIR / "Applications" / "I_P.py"
        try:
            subprocess.Popen([str(python_path), str(script_path)])
        except Exception as e:
            print(f"Failed to open {script_path}: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Create the application instance
    window = MainDashboard()  # Create the main window
    window.show()  # Show the window
    sys.exit(app.exec())  # Execute the application
