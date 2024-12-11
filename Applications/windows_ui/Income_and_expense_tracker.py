# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Income_and _expense_tracker.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpinBox, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_IncomeAndExpenseTracker(object):
    def setupUi(self, IncomeAndExpenseTracker):
        if not IncomeAndExpenseTracker.objectName():
            IncomeAndExpenseTracker.setObjectName(u"IncomeAndExpenseTracker")
        IncomeAndExpenseTracker.resize(836, 475)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        IncomeAndExpenseTracker.setFont(font)
        IncomeAndExpenseTracker.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        IncomeAndExpenseTracker.setMouseTracking(False)
        self.centralwidget = QWidget(IncomeAndExpenseTracker)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gb_Inputs_and_display = QGroupBox(self.centralwidget)
        self.gb_Inputs_and_display.setObjectName(u"gb_Inputs_and_display")
        self.gb_Inputs_and_display.setEnabled(True)
        self.gb_Inputs_and_display.setGeometry(QRect(10, 0, 591, 441))
        self.gb_Inputs_and_display.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.gridLayoutWidget = QWidget(self.gb_Inputs_and_display)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 20, 581, 151))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cb_Expense_Category = QComboBox(self.gridLayoutWidget)
        self.cb_Expense_Category.addItem("")
        self.cb_Expense_Category.addItem("")
        self.cb_Expense_Category.addItem("")
        self.cb_Expense_Category.addItem("")
        self.cb_Expense_Category.setObjectName(u"cb_Expense_Category")
        self.cb_Expense_Category.setEnabled(True)
        self.cb_Expense_Category.setToolTipDuration(-2)
        self.cb_Expense_Category.setEditable(True)

        self.gridLayout.addWidget(self.cb_Expense_Category, 1, 3, 1, 1)

        self.pb_Income = QPushButton(self.gridLayoutWidget)
        self.pb_Income.setObjectName(u"pb_Income")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.pb_Income.setIcon(icon)

        self.gridLayout.addWidget(self.pb_Income, 0, 4, 1, 1)

        self.pb_Expense = QPushButton(self.gridLayoutWidget)
        self.pb_Expense.setObjectName(u"pb_Expense")
        self.pb_Expense.setIcon(icon)

        self.gridLayout.addWidget(self.pb_Expense, 1, 4, 1, 1)

        self.le_Income = QLineEdit(self.gridLayoutWidget)
        self.le_Income.setObjectName(u"le_Income")
        self.le_Income.setMaxLength(32767)

        self.gridLayout.addWidget(self.le_Income, 0, 2, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.sb_Budget = QSpinBox(self.gridLayoutWidget)
        self.sb_Budget.setObjectName(u"sb_Budget")
        self.sb_Budget.setWrapping(False)
        self.sb_Budget.setFrame(True)
        self.sb_Budget.setMaximum(1000000)
        self.sb_Budget.setSingleStep(100)

        self.gridLayout.addWidget(self.sb_Budget, 2, 2, 1, 1)

        self.pb_Budget = QPushButton(self.gridLayoutWidget)
        self.pb_Budget.setObjectName(u"pb_Budget")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SystemLogOut))
        self.pb_Budget.setIcon(icon1)

        self.gridLayout.addWidget(self.pb_Budget, 2, 4, 1, 1)

        self.cb_Budget_Category = QComboBox(self.gridLayoutWidget)
        self.cb_Budget_Category.addItem("")
        self.cb_Budget_Category.addItem("")
        self.cb_Budget_Category.addItem("")
        self.cb_Budget_Category.addItem("")
        self.cb_Budget_Category.setObjectName(u"cb_Budget_Category")
        self.cb_Budget_Category.setEnabled(True)
        self.cb_Budget_Category.setToolTipDuration(-2)
        self.cb_Budget_Category.setEditable(True)

        self.gridLayout.addWidget(self.cb_Budget_Category, 2, 3, 1, 1)

        self.sb_Expense = QSpinBox(self.gridLayoutWidget)
        self.sb_Expense.setObjectName(u"sb_Expense")
        self.sb_Expense.setWrapping(False)
        self.sb_Expense.setFrame(True)
        self.sb_Expense.setMaximum(1000000)
        self.sb_Expense.setSingleStep(100)

        self.gridLayout.addWidget(self.sb_Expense, 1, 2, 1, 1)

        self.tw_Summary = QTableWidget(self.gb_Inputs_and_display)
        if (self.tw_Summary.columnCount() < 5):
            self.tw_Summary.setColumnCount(5)
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tw_Summary.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.tw_Summary.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font2);
        self.tw_Summary.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font2);
        self.tw_Summary.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font2);
        self.tw_Summary.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tw_Summary.setObjectName(u"tw_Summary")
        self.tw_Summary.setGeometry(QRect(5, 171, 591, 171))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tw_Summary.sizePolicy().hasHeightForWidth())
        self.tw_Summary.setSizePolicy(sizePolicy)
        self.tw_Summary.setAlternatingRowColors(True)
        self.tw_Summary.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.tw_Summary.setRowCount(0)
        self.tw_Summary.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tw_Summary.horizontalHeader().setStretchLastSection(True)
        self.tw_Summary.verticalHeader().setProperty(u"showSortIndicator", False)
        self.l_Total_Income = QLabel(self.gb_Inputs_and_display)
        self.l_Total_Income.setObjectName(u"l_Total_Income")
        self.l_Total_Income.setGeometry(QRect(0, 360, 271, 31))
        self.l_Total_Expenses = QLabel(self.gb_Inputs_and_display)
        self.l_Total_Expenses.setObjectName(u"l_Total_Expenses")
        self.l_Total_Expenses.setGeometry(QRect(280, 360, 311, 31))
        self.l_Debt = QLabel(self.gb_Inputs_and_display)
        self.l_Debt.setObjectName(u"l_Debt")
        self.l_Debt.setGeometry(QRect(280, 400, 311, 31))
        self.gb_Results = QGroupBox(self.centralwidget)
        self.gb_Results.setObjectName(u"gb_Results")
        self.gb_Results.setGeometry(QRect(610, 0, 221, 401))
        self.verticalLayoutWidget = QWidget(self.gb_Results)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 30, 244, 301))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.l_Net_Income = QLabel(self.verticalLayoutWidget)
        self.l_Net_Income.setObjectName(u"l_Net_Income")

        self.verticalLayout.addWidget(self.l_Net_Income)

        self.l_Budget_Surplus = QLabel(self.verticalLayoutWidget)
        self.l_Budget_Surplus.setObjectName(u"l_Budget_Surplus")

        self.verticalLayout.addWidget(self.l_Budget_Surplus)

        self.l_Savings_Rate = QLabel(self.verticalLayoutWidget)
        self.l_Savings_Rate.setObjectName(u"l_Savings_Rate")

        self.verticalLayout.addWidget(self.l_Savings_Rate)

        self.l_Emergency_Funds = QLabel(self.verticalLayoutWidget)
        self.l_Emergency_Funds.setObjectName(u"l_Emergency_Funds")

        self.verticalLayout.addWidget(self.l_Emergency_Funds)

        self.pb_Extract = QPushButton(self.gb_Results)
        self.pb_Extract.setObjectName(u"pb_Extract")
        self.pb_Extract.setGeometry(QRect(0, 350, 211, 31))
        self.pb_Extract.setAutoFillBackground(True)
        self.l_Status = QLabel(self.centralwidget)
        self.l_Status.setObjectName(u"l_Status")
        self.l_Status.setGeometry(QRect(610, 410, 221, 31))
        self.l_Total_Budget = QLabel(self.centralwidget)
        self.l_Total_Budget.setObjectName(u"l_Total_Budget")
        self.l_Total_Budget.setGeometry(QRect(10, 400, 271, 31))
        IncomeAndExpenseTracker.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(IncomeAndExpenseTracker)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 836, 24))
        IncomeAndExpenseTracker.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(IncomeAndExpenseTracker)
        self.statusbar.setObjectName(u"statusbar")
        IncomeAndExpenseTracker.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.sb_Budget, self.pb_Budget)
        QWidget.setTabOrder(self.pb_Budget, self.le_Income)
        QWidget.setTabOrder(self.le_Income, self.pb_Income)
        QWidget.setTabOrder(self.pb_Income, self.cb_Expense_Category)
        QWidget.setTabOrder(self.cb_Expense_Category, self.pb_Expense)
        QWidget.setTabOrder(self.pb_Expense, self.tw_Summary)
        QWidget.setTabOrder(self.tw_Summary, self.pb_Extract)

        self.retranslateUi(IncomeAndExpenseTracker)

        QMetaObject.connectSlotsByName(IncomeAndExpenseTracker)
    # setupUi

    def retranslateUi(self, IncomeAndExpenseTracker):
        IncomeAndExpenseTracker.setWindowTitle(QCoreApplication.translate("IncomeAndExpenseTracker", u"Income and Expense Tracker", None))
        self.gb_Inputs_and_display.setTitle(QCoreApplication.translate("IncomeAndExpenseTracker", u"Income and Expense Tracker", None))
        self.cb_Expense_Category.setItemText(0, QCoreApplication.translate("IncomeAndExpenseTracker", u"Rent", None))
        self.cb_Expense_Category.setItemText(1, QCoreApplication.translate("IncomeAndExpenseTracker", u"Utilities", None))
        self.cb_Expense_Category.setItemText(2, QCoreApplication.translate("IncomeAndExpenseTracker", u"Groceries", None))
        self.cb_Expense_Category.setItemText(3, QCoreApplication.translate("IncomeAndExpenseTracker", u"Entertainment", None))

#if QT_CONFIG(tooltip)
        self.cb_Expense_Category.setToolTip(QCoreApplication.translate("IncomeAndExpenseTracker", u"select of type category for expense", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Expense_Category.setCurrentText("")
        self.cb_Expense_Category.setPlaceholderText(QCoreApplication.translate("IncomeAndExpenseTracker", u"category", None))
        self.pb_Income.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Add", None))
        self.pb_Expense.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Add", None))
        self.le_Income.setText("")
        self.le_Income.setPlaceholderText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Enter the Income Amount", None))
        self.label.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Add Income Amount", None))
        self.label_2.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Add Expense Amount", None))
        self.label_3.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Set Budget Amount", None))
#if QT_CONFIG(tooltip)
        self.sb_Budget.setToolTip(QCoreApplication.translate("IncomeAndExpenseTracker", u"enter the monthly budget", None))
#endif // QT_CONFIG(tooltip)
        self.sb_Budget.setSuffix(QCoreApplication.translate("IncomeAndExpenseTracker", u"  \u20b9", None))
        self.pb_Budget.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Set", None))
        self.cb_Budget_Category.setItemText(0, QCoreApplication.translate("IncomeAndExpenseTracker", u"Rent", None))
        self.cb_Budget_Category.setItemText(1, QCoreApplication.translate("IncomeAndExpenseTracker", u"Utilities", None))
        self.cb_Budget_Category.setItemText(2, QCoreApplication.translate("IncomeAndExpenseTracker", u"Groceries", None))
        self.cb_Budget_Category.setItemText(3, QCoreApplication.translate("IncomeAndExpenseTracker", u"Entertainment", None))

#if QT_CONFIG(tooltip)
        self.cb_Budget_Category.setToolTip(QCoreApplication.translate("IncomeAndExpenseTracker", u"select of type category for expense", None))
#endif // QT_CONFIG(tooltip)
        self.cb_Budget_Category.setCurrentText("")
        self.cb_Budget_Category.setPlaceholderText(QCoreApplication.translate("IncomeAndExpenseTracker", u"category", None))
#if QT_CONFIG(tooltip)
        self.sb_Expense.setToolTip(QCoreApplication.translate("IncomeAndExpenseTracker", u"enter the monthly budget", None))
#endif // QT_CONFIG(tooltip)
        self.sb_Expense.setSuffix(QCoreApplication.translate("IncomeAndExpenseTracker", u"  \u20b9", None))
        ___qtablewidgetitem = self.tw_Summary.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Type", None));
        ___qtablewidgetitem1 = self.tw_Summary.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Category", None));
        ___qtablewidgetitem2 = self.tw_Summary.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Budget", None));
        ___qtablewidgetitem3 = self.tw_Summary.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Expenditure", None));
        ___qtablewidgetitem4 = self.tw_Summary.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Net", None));
        self.l_Total_Income.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Total Income: \u20b9 0 ", None))
        self.l_Total_Expenses.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Total Expenses: \u20b9 0", None))
        self.l_Debt.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Debt: \u20b9 0", None))
        self.gb_Results.setTitle(QCoreApplication.translate("IncomeAndExpenseTracker", u"Resulting Metrics", None))
        self.l_Net_Income.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Net Income: \u20b9 0", None))
        self.l_Budget_Surplus.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Budget Surplus: \u20b9 0", None))
        self.l_Savings_Rate.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Savings Rate: 0.0 %", None))
        self.l_Emergency_Funds.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Emergency Funds: \u20b9 0", None))
        self.pb_Extract.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Extract PDF", None))
        self.l_Status.setText("")
        self.l_Total_Budget.setText(QCoreApplication.translate("IncomeAndExpenseTracker", u"Total Budget: \u20b9 0", None))
    # retranslateUi

