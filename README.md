
# FinSight

FinSight is an intuitive and robust desktop application designed to simplify financial management for individuals and businesses. It offers three core modules:

**Income and Expense Tracker:** Helps users log and monitor their income, budgets, and expenditures. It provides insights into financial health with detailed metrics like net income, savings rate, and debt.

**Analysis and Recommendations:** Analyzes financial data to predict trends and offer actionable recommendations, empowering users to make informed decisions.

**Investment Portfolio Manager:** Tracks and visualizes asset performance over time, generating insights and reports for smarter investment strategies.

The application is built with Python and PySide6 for a sleek, modern interface, supports dynamic file paths for easy portability, and integrates seamlessly with CSV, JSON, and PDF formats for data storage and reporting. Designed for usability and efficiency, FinSight empowers users to take control of their financial journey.


## Acknowledgements

 - [Google Finance API Documentation](https://www.searchapi.io/docs/google-finance)
 - [Pyside6/PyQT6 Documentation](https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/index.html)
 - [Link to FOSSEE IIT Bombay](https://fossee.in/)
 - [Link to JNTUH College of Engineering Sultanpur](https://www.jntuhces.ac.in/)

## Installation and Run Locally

- To run this project, we need to install virtual environment to install the dependencies:

```bash
  pip install virtualenv
```
- Then instantiate the virtual environment with command:

```bash
  virtualenv <environment name>
```
- Then move to the virtual environment and activate it:

```bash
  <environment name>\Scripts\activate
```

- Then we initialize the git

```bash
  git init 
```

- Then we clone the repository into the project location in the same level of the environment file

```bash
  git clone https://github.com/hydracsnova13/FinSight-Desktop-Application.git
```
- Then we signup into Google Search API with the link: https://www.searchapi.io/ and get the API key to activate the investment Portfolio API when running the application

- Copy the API key and paste it in the slot provided in the code I_P.py in the location of line number 380, below is what the line of code looks like:

```bash
  self.api_key = "ENTER API KEY"
```

- Then go to the Applications folder

```bash
  cd Applications
```

- Then install the dependencies using the command:

```bash
  pip install -r requirements.txt
```

- Then after Installation we run the application using the command:

```bash
  python Dashboard.py
```
- Then the application window will open with 3 buttons for the three subwindows have opened which can be clicked to navigate among the application

## Features

- Income and Expense tracking
- Live price updates
- API integration for insights on assets and their trends
- Make trends in expenditure and savings rate
- Make predictions on the expnditure and savings rate
- Live asset trends and news updates with insights
- Track and maintain consistent dataset of your expenses
- Display accurate metrics to assess one's expense and savings with analysis charts
- Extract all the information into pdf's to store and send to other users if needed
- Status display to check if any issues arise
- Detailed logging of all the events that take place while operating the application
- Display tables for easy manipulation of dataset
- Interactive and functional User Interface
- Give accurate predicted expeness for the next month in row(minimum 12 months needed to start predicting)
- Get insights on expenditure and savings rate for effective management of portfolio of expediture
- Efficient management Fintech Resources

## License

[MIT](https://github.com/hydracsnova13/FinSight-Desktop-Application/blob/main/LICENSE)

