# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Finsight_Dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import icons_rc

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.setWindowModality(Qt.WindowModality.ApplicationModal)
        Dashboard.resize(634, 484)
        base_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pb_Income_Expense = QPushButton(self.centralwidget)
        self.pb_Income_Expense.setObjectName(u"pb_Income_Expense")
        self.pb_Income_Expense.setGeometry(QRect(20, 80, 311, 121))
        self.pb_Income_Expense.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        self.pb_Income_Expense.setFont(font)
        self.pb_Income_Expense.setMouseTracking(False)
        self.pb_Analyze_Recommend = QPushButton(self.centralwidget)
        self.pb_Analyze_Recommend.setObjectName(u"pb_Analyze_Recommend")
        self.pb_Analyze_Recommend.setGeometry(QRect(20, 210, 311, 121))
        self.pb_Analyze_Recommend.setFont(font)
        self.pb_Investment_Portfolio = QPushButton(self.centralwidget)
        self.pb_Investment_Portfolio.setObjectName(u"pb_Investment_Portfolio")
        self.pb_Investment_Portfolio.setGeometry(QRect(20, 340, 311, 121))
        self.pb_Investment_Portfolio.setFont(font)
        
        self.pb_Income_Expense.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        self.pb_Analyze_Recommend.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        self.pb_Investment_Portfolio.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
        """)

        self.pb_Income_Expense.setIconSize(QSize(50, 50))
        
        self.l_App_Name = QLabel(self.centralwidget)
        self.l_App_Name.setObjectName(u"l_App_Name")
        self.l_App_Name.setGeometry(QRect(240, 10, 171, 51))
        font1 = QFont()
        font1.setFamilies([u"Stencil"])
        font1.setPointSize(26)
        font1.setItalic(False)
        self.l_App_Name.setFont(font1)
        self.l_App_Name.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.l_App_Name.setAutoFillBackground(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(440, 80, 121, 121))
        self.label.setPixmap(QPixmap(os.path.join(base_directory, "Income&Expense.png")))
        self.label.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(430, 210, 121, 121))
        self.label_2.setAutoFillBackground(True)
        self.label_2.setPixmap(QPixmap(os.path.join(base_directory, "Analyze&Recommend.png")))
        self.label_2.setScaledContents(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(400, 340, 171, 121))
        self.label_3.setPixmap(QPixmap(os.path.join(base_directory, "InvestmentPortfolio.png")))
        self.label_3.setScaledContents(True)
        Dashboard.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)

        self.pb_Income_Expense.setDefault(False)


        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"FinSight Dashboard", None))
        self.pb_Income_Expense.setText(QCoreApplication.translate("Dashboard", u"Income and Expense Tracker", None))
        self.pb_Analyze_Recommend.setText(QCoreApplication.translate("Dashboard", u"Analyze and Predict", None))
        self.pb_Investment_Portfolio.setText(QCoreApplication.translate("Dashboard", u"Investment Portfolio", None))
        self.l_App_Name.setText(QCoreApplication.translate("Dashboard", u"FinSight", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

