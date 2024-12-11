# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Investment_Portfolio.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpinBox, QStatusBar, QTableView, QWidget)

class Ui_Investment_Portfolio(object):
    def setupUi(self, Investment_Portfolio):
        if not Investment_Portfolio.objectName():
            Investment_Portfolio.setObjectName(u"Investment_Portfolio")
        Investment_Portfolio.resize(1097, 552)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(11)
        Investment_Portfolio.setFont(font)
        self.centralwidget = QWidget(Investment_Portfolio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setFont(font)
        self.gb_Investment_Portfolio = QGroupBox(self.centralwidget)
        self.gb_Investment_Portfolio.setObjectName(u"gb_Investment_Portfolio")
        self.gb_Investment_Portfolio.setGeometry(QRect(10, 0, 701, 511))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setItalic(False)
        self.gb_Investment_Portfolio.setFont(font1)
        self.gb_Investment_Portfolio.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.ab_Assets_input = QGroupBox(self.gb_Investment_Portfolio)
        self.ab_Assets_input.setObjectName(u"ab_Assets_input")
        self.ab_Assets_input.setGeometry(QRect(10, 20, 381, 211))
        self.ab_Assets_input.setFont(font1)
        self.gridLayoutWidget = QWidget(self.ab_Assets_input)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 30, 361, 171))
        self.gl_Assets_Input = QGridLayout(self.gridLayoutWidget)
        self.gl_Assets_Input.setObjectName(u"gl_Assets_Input")
        self.gl_Assets_Input.setContentsMargins(0, 0, 0, 0)
        self.cb_Sub_Category_Selection = QComboBox(self.gridLayoutWidget)
        self.cb_Sub_Category_Selection.setObjectName(u"cb_Sub_Category_Selection")
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        self.cb_Sub_Category_Selection.setFont(font2)

        self.gl_Assets_Input.addWidget(self.cb_Sub_Category_Selection, 2, 1, 1, 1)

        self.l_Sub_Category_1 = QLabel(self.gridLayoutWidget)
        self.l_Sub_Category_1.setObjectName(u"l_Sub_Category_1")
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setItalic(True)
        self.l_Sub_Category_1.setFont(font3)

        self.gl_Assets_Input.addWidget(self.l_Sub_Category_1, 2, 0, 1, 1)

        self.cb_Asset_Types = QComboBox(self.gridLayoutWidget)
        self.cb_Asset_Types.addItem("")
        self.cb_Asset_Types.addItem("")
        self.cb_Asset_Types.addItem("")
        self.cb_Asset_Types.setObjectName(u"cb_Asset_Types")
        self.cb_Asset_Types.setFont(font2)
        self.cb_Asset_Types.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

        self.gl_Assets_Input.addWidget(self.cb_Asset_Types, 0, 1, 1, 1)

        self.l_Asset_Name = QLabel(self.gridLayoutWidget)
        self.l_Asset_Name.setObjectName(u"l_Asset_Name")
        self.l_Asset_Name.setFont(font3)

        self.gl_Assets_Input.addWidget(self.l_Asset_Name, 1, 0, 1, 1)

        self.l_Asset_Type = QLabel(self.gridLayoutWidget)
        self.l_Asset_Type.setObjectName(u"l_Asset_Type")
        self.l_Asset_Type.setFont(font3)

        self.gl_Assets_Input.addWidget(self.l_Asset_Type, 0, 0, 1, 1)

        self.l_Quantitative_Category = QLabel(self.gridLayoutWidget)
        self.l_Quantitative_Category.setObjectName(u"l_Quantitative_Category")
        self.l_Quantitative_Category.setFont(font3)

        self.gl_Assets_Input.addWidget(self.l_Quantitative_Category, 3, 0, 1, 1)

        self.sb_Quantitative_Category = QSpinBox(self.gridLayoutWidget)
        self.sb_Quantitative_Category.setObjectName(u"sb_Quantitative_Category")
        self.sb_Quantitative_Category.setFont(font2)
        self.sb_Quantitative_Category.setMaximum(10000)

        self.gl_Assets_Input.addWidget(self.sb_Quantitative_Category, 3, 1, 1, 1)

        self.cb_Asset_Name = QComboBox(self.gridLayoutWidget)
        self.cb_Asset_Name.setObjectName(u"cb_Asset_Name")
        self.cb_Asset_Name.setFont(font2)

        self.gl_Assets_Input.addWidget(self.cb_Asset_Name, 1, 1, 1, 1)

        self.tv_Assets_Status_Display = QTableView(self.gb_Investment_Portfolio)
        self.tv_Assets_Status_Display.setObjectName(u"tv_Assets_Status_Display")
        self.tv_Assets_Status_Display.setGeometry(QRect(400, 30, 291, 201))
        self.tv_Assets_Status_Display.setFont(font2)
        self.pb_Extract_Portfolio = QPushButton(self.gb_Investment_Portfolio)
        self.pb_Extract_Portfolio.setObjectName(u"pb_Extract_Portfolio")
        self.pb_Extract_Portfolio.setGeometry(QRect(10, 240, 181, 31))
        self.f_Progress_Line_Graph = QFrame(self.gb_Investment_Portfolio)
        self.f_Progress_Line_Graph.setObjectName(u"f_Progress_Line_Graph")
        self.f_Progress_Line_Graph.setGeometry(QRect(10, 280, 681, 221))
        self.f_Progress_Line_Graph.setFrameShape(QFrame.Shape.StyledPanel)
        self.f_Progress_Line_Graph.setFrameShadow(QFrame.Shadow.Raised)
        self.pb_Add_Asset = QPushButton(self.gb_Investment_Portfolio)
        self.pb_Add_Asset.setObjectName(u"pb_Add_Asset")
        self.pb_Add_Asset.setGeometry(QRect(200, 240, 91, 31))
        self.l_Status = QLabel(self.gb_Investment_Portfolio)
        self.l_Status.setObjectName(u"l_Status")
        self.l_Status.setGeometry(QRect(410, 240, 281, 31))
        self.pb_Remove_Asset = QPushButton(self.gb_Investment_Portfolio)
        self.pb_Remove_Asset.setObjectName(u"pb_Remove_Asset")
        self.pb_Remove_Asset.setGeometry(QRect(300, 240, 101, 31))
        self.gb_Insights = QGroupBox(self.centralwidget)
        self.gb_Insights.setObjectName(u"gb_Insights")
        self.gb_Insights.setGeometry(QRect(720, 0, 371, 511))
        self.sa_Insights = QScrollArea(self.gb_Insights)
        self.sa_Insights.setObjectName(u"sa_Insights")
        self.sa_Insights.setGeometry(QRect(10, 30, 351, 471))
        self.sa_Insights.setFrameShape(QFrame.Shape.StyledPanel)
        self.sa_Insights.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 349, 469))
        self.sa_Insights.setWidget(self.scrollAreaWidgetContents)
        Investment_Portfolio.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Investment_Portfolio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1097, 23))
        Investment_Portfolio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Investment_Portfolio)
        self.statusbar.setObjectName(u"statusbar")
        Investment_Portfolio.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.cb_Asset_Types, self.cb_Sub_Category_Selection)
        QWidget.setTabOrder(self.cb_Sub_Category_Selection, self.sb_Quantitative_Category)
        QWidget.setTabOrder(self.sb_Quantitative_Category, self.pb_Extract_Portfolio)
        QWidget.setTabOrder(self.pb_Extract_Portfolio, self.pb_Add_Asset)
        QWidget.setTabOrder(self.pb_Add_Asset, self.pb_Remove_Asset)
        QWidget.setTabOrder(self.pb_Remove_Asset, self.tv_Assets_Status_Display)

        self.retranslateUi(Investment_Portfolio)

        QMetaObject.connectSlotsByName(Investment_Portfolio)
    # setupUi

    def retranslateUi(self, Investment_Portfolio):
        Investment_Portfolio.setWindowTitle(QCoreApplication.translate("Investment_Portfolio", u"Investment Portfolio", None))
        self.gb_Investment_Portfolio.setTitle(QCoreApplication.translate("Investment_Portfolio", u"Investment Portfolio", None))
        self.ab_Assets_input.setTitle(QCoreApplication.translate("Investment_Portfolio", u"Add Assets to Track", None))
        self.l_Sub_Category_1.setText(QCoreApplication.translate("Investment_Portfolio", u"Select subcategory 1", None))
        self.cb_Asset_Types.setItemText(0, QCoreApplication.translate("Investment_Portfolio", u"Stock", None))
        self.cb_Asset_Types.setItemText(1, QCoreApplication.translate("Investment_Portfolio", u"Mutual Funds", None))
        self.cb_Asset_Types.setItemText(2, QCoreApplication.translate("Investment_Portfolio", u"Currency", None))

        self.cb_Asset_Types.setCurrentText(QCoreApplication.translate("Investment_Portfolio", u"Stock", None))
        self.l_Asset_Name.setText(QCoreApplication.translate("Investment_Portfolio", u"Name Of Asset", None))
        self.l_Asset_Type.setText(QCoreApplication.translate("Investment_Portfolio", u"Add Asset Type", None))
        self.l_Quantitative_Category.setText("")
        self.pb_Extract_Portfolio.setText(QCoreApplication.translate("Investment_Portfolio", u"Extract Portfolio Progress", None))
        self.pb_Add_Asset.setText(QCoreApplication.translate("Investment_Portfolio", u"Add Asset", None))
        self.l_Status.setText("")
        self.pb_Remove_Asset.setText(QCoreApplication.translate("Investment_Portfolio", u"Remove Asset", None))
        self.gb_Insights.setTitle(QCoreApplication.translate("Investment_Portfolio", u"Insights", None))
#if QT_CONFIG(tooltip)
        self.sa_Insights.setToolTip(QCoreApplication.translate("Investment_Portfolio", u"Provide the insights on the assets", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

