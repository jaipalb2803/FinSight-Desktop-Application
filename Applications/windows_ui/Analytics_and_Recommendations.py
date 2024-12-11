# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Analytics_and_Recommendations.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QWidget)

class Ui_Analytics_and_Recommendations(object):
    def setupUi(self, Analytics_and_Recommendations):
        if not Analytics_and_Recommendations.objectName():
            Analytics_and_Recommendations.setObjectName(u"Analytics_and_Recommendations")
        Analytics_and_Recommendations.resize(721, 550)
        self.centralwidget = QWidget(Analytics_and_Recommendations)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gb_Analytics = QGroupBox(self.centralwidget)
        self.gb_Analytics.setObjectName(u"gb_Analytics")
        self.gb_Analytics.setGeometry(QRect(10, 0, 701, 521))
        self.gb_Analytics.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.gb_Analytics.setFlat(False)
        self.gb_Analytics.setCheckable(False)
        self.f_Line_Graph = QFrame(self.gb_Analytics)
        self.f_Line_Graph.setObjectName(u"f_Line_Graph")
        self.f_Line_Graph.setGeometry(QRect(170, 30, 511, 231))
        self.f_Line_Graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_Line_Graph.setFrameShadow(QFrame.Shadow.Raised)
        self.f_Pie_Graph = QFrame(self.gb_Analytics)
        self.f_Pie_Graph.setObjectName(u"f_Pie_Graph")
        self.f_Pie_Graph.setGeometry(QRect(440, 310, 241, 151))
        self.f_Pie_Graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_Pie_Graph.setFrameShadow(QFrame.Shadow.Raised)
        self.gb_Predicted_expenses = QGroupBox(self.gb_Analytics)
        self.gb_Predicted_expenses.setObjectName(u"gb_Predicted_expenses")
        self.gb_Predicted_expenses.setGeometry(QRect(10, 20, 151, 471))
        self.gb_Predicted_expenses.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sa_Predicted_Expenses = QScrollArea(self.gb_Predicted_expenses)
        self.sa_Predicted_Expenses.setObjectName(u"sa_Predicted_Expenses")
        self.sa_Predicted_Expenses.setGeometry(QRect(10, 20, 131, 441))
        self.sa_Predicted_Expenses.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 129, 439))
        self.sa_Predicted_Expenses.setWidget(self.scrollAreaWidgetContents_2)
        self.gb_Insights = QGroupBox(self.gb_Analytics)
        self.gb_Insights.setObjectName(u"gb_Insights")
        self.gb_Insights.setGeometry(QRect(170, 300, 261, 191))
        self.gb_Insights.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sa_Insights = QScrollArea(self.gb_Insights)
        self.sa_Insights.setObjectName(u"sa_Insights")
        self.sa_Insights.setGeometry(QRect(10, 20, 241, 161))
        self.sa_Insights.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 239, 159))
        self.sa_Insights.setWidget(self.scrollAreaWidgetContents)
        self.pb_Export_Analytics = QPushButton(self.gb_Analytics)
        self.pb_Export_Analytics.setObjectName(u"pb_Export_Analytics")
        self.pb_Export_Analytics.setGeometry(QRect(430, 270, 121, 31))
        self.l_Status = QLabel(self.gb_Analytics)
        self.l_Status.setObjectName(u"l_Status")
        self.l_Status.setGeometry(QRect(440, 470, 241, 21))
        self.pb_Projection = QPushButton(self.gb_Analytics)
        self.pb_Projection.setObjectName(u"pb_Projection")
        self.pb_Projection.setGeometry(QRect(170, 270, 121, 31))
        self.pb_Past_Data_Visualize = QPushButton(self.gb_Analytics)
        self.pb_Past_Data_Visualize.setObjectName(u"pb_Past_Data_Visualize")
        self.pb_Past_Data_Visualize.setGeometry(QRect(300, 270, 121, 31))
        self.pb_Export_Predictions = QPushButton(self.gb_Analytics)
        self.pb_Export_Predictions.setObjectName(u"pb_Export_Predictions")
        self.pb_Export_Predictions.setGeometry(QRect(560, 270, 121, 31))
        Analytics_and_Recommendations.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Analytics_and_Recommendations)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 721, 22))
        Analytics_and_Recommendations.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Analytics_and_Recommendations)
        self.statusbar.setObjectName(u"statusbar")
        Analytics_and_Recommendations.setStatusBar(self.statusbar)

        self.retranslateUi(Analytics_and_Recommendations)

        QMetaObject.connectSlotsByName(Analytics_and_Recommendations)
    # setupUi

    def retranslateUi(self, Analytics_and_Recommendations):
        Analytics_and_Recommendations.setWindowTitle(QCoreApplication.translate("Analytics_and_Recommendations", u"Analytics and Recommendations", None))
        self.gb_Analytics.setTitle(QCoreApplication.translate("Analytics_and_Recommendations", u"Analytics and Recommendations ", None))
        self.gb_Predicted_expenses.setTitle(QCoreApplication.translate("Analytics_and_Recommendations", u"Predicted Expenses", None))
#if QT_CONFIG(tooltip)
        self.sa_Predicted_Expenses.setToolTip(QCoreApplication.translate("Analytics_and_Recommendations", u"<html><head/><body><p>Predicted Values of Expenses According to Past Expenses</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.gb_Insights.setTitle(QCoreApplication.translate("Analytics_and_Recommendations", u"Insights", None))
#if QT_CONFIG(tooltip)
        self.sa_Insights.setToolTip(QCoreApplication.translate("Analytics_and_Recommendations", u"<html><head/><body><p>Insights Based on the Past Data</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pb_Export_Analytics.setToolTip(QCoreApplication.translate("Analytics_and_Recommendations", u"<html><head/><body><p>Export in PDF format</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_Export_Analytics.setText(QCoreApplication.translate("Analytics_and_Recommendations", u"Export Analytics", None))
        self.l_Status.setText("")
        self.pb_Projection.setText(QCoreApplication.translate("Analytics_and_Recommendations", u"Predict", None))
#if QT_CONFIG(tooltip)
        self.pb_Past_Data_Visualize.setToolTip(QCoreApplication.translate("Analytics_and_Recommendations", u"<html><head/><body><p>Analyze your past data and also press again to get the legend for the graph</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_Past_Data_Visualize.setText(QCoreApplication.translate("Analytics_and_Recommendations", u"Analyze", None))
#if QT_CONFIG(tooltip)
        self.pb_Export_Predictions.setToolTip(QCoreApplication.translate("Analytics_and_Recommendations", u"<html><head/><body><p>Export in PDF format</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pb_Export_Predictions.setText(QCoreApplication.translate("Analytics_and_Recommendations", u"Export Predictions", None))
    # retranslateUi

