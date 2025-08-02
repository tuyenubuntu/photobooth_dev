# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QToolBar, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1362, 884)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1362, 884))
        MainWindow.setStyleSheet(u"QPushButton#Main_Button {\n"
"    background-color: rgb(80, 159, 239);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1314, 818))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    \n"
"	background-image: url(./statics/background.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_navbar = QWidget(self.centralwidget)
        self.widget_navbar.setObjectName(u"widget_navbar")
        sizePolicy.setHeightForWidth(self.widget_navbar.sizePolicy().hasHeightForWidth())
        self.widget_navbar.setSizePolicy(sizePolicy)
        self.widget_navbar.setMaximumSize(QSize(16777215, 61))
        self.verticalLayout_2 = QVBoxLayout(self.widget_navbar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_img = QLabel(self.widget_navbar)
        self.header_img.setObjectName(u"header_img")
        sizePolicy.setHeightForWidth(self.header_img.sizePolicy().hasHeightForWidth())
        self.header_img.setSizePolicy(sizePolicy)
        self.header_img.setMinimumSize(QSize(1321, 16))
        self.header_img.setMaximumSize(QSize(16777215, 16))
        self.header_img.setPixmap(QPixmap(u"statics/header.jpg"))
        self.header_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.header_img, 0, Qt.AlignmentFlag.AlignTop)

        self.navbar = QWidget(self.widget_navbar)
        self.navbar.setObjectName(u"navbar")
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setMinimumSize(QSize(1321, 51))
        self.navbar.setMaximumSize(QSize(16777215, 51))
        self.navbar.setAutoFillBackground(False)
        self.navbar.setStyleSheet(u"QWidget#navbar {\n"
"    background-color: rgb(170, 255, 127);  \n"
"    color: white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.navbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_img = QLabel(self.navbar)
        self.logo_img.setObjectName(u"logo_img")
        sizePolicy.setHeightForWidth(self.logo_img.sizePolicy().hasHeightForWidth())
        self.logo_img.setSizePolicy(sizePolicy)
        self.logo_img.setMinimumSize(QSize(61, 31))
        self.logo_img.setMaximumSize(QSize(61, 31))
        self.logo_img.setPixmap(QPixmap(u"statics/logo.png"))
        self.logo_img.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo_img)

        self.Manual_Button = QPushButton(self.navbar)
        self.Manual_Button.setObjectName(u"Manual_Button")
        sizePolicy.setHeightForWidth(self.Manual_Button.sizePolicy().hasHeightForWidth())
        self.Manual_Button.setSizePolicy(sizePolicy)
        self.Manual_Button.setMinimumSize(QSize(101, 31))
        self.Manual_Button.setMaximumSize(QSize(101, 31))
        self.Manual_Button.setStyleSheet(u"QPushButton#Manual_Button {\n"
"    background-color: rgb(77, 155, 232);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Manual_Button)

        self.Instruction_Button = QPushButton(self.navbar)
        self.Instruction_Button.setObjectName(u"Instruction_Button")
        sizePolicy.setHeightForWidth(self.Instruction_Button.sizePolicy().hasHeightForWidth())
        self.Instruction_Button.setSizePolicy(sizePolicy)
        self.Instruction_Button.setMinimumSize(QSize(101, 31))
        self.Instruction_Button.setMaximumSize(QSize(101, 31))
        self.Instruction_Button.setStyleSheet(u"QPushButton#Instruction_Button {\n"
"    background-color: rgb(77, 155, 232);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Instruction_Button)

        self.name_application = QLabel(self.navbar)
        self.name_application.setObjectName(u"name_application")
        sizePolicy.setHeightForWidth(self.name_application.sizePolicy().hasHeightForWidth())
        self.name_application.setSizePolicy(sizePolicy)
        self.name_application.setMinimumSize(QSize(725, 33))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(True)
        self.name_application.setFont(font)
        self.name_application.setStyleSheet(u"QLabel#name_application{\n"
"    color: black;\n"
"}")
        self.name_application.setScaledContents(True)

        self.horizontalLayout.addWidget(self.name_application)

        self.Login_Button = QPushButton(self.navbar)
        self.Login_Button.setObjectName(u"Login_Button")
        sizePolicy.setHeightForWidth(self.Login_Button.sizePolicy().hasHeightForWidth())
        self.Login_Button.setSizePolicy(sizePolicy)
        self.Login_Button.setMinimumSize(QSize(101, 31))
        self.Login_Button.setMaximumSize(QSize(101, 31))
        self.Login_Button.setStyleSheet(u"QPushButton#Login_Button {\n"
"    background-color: rgb(77, 155, 232);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.Login_Button)


        self.verticalLayout_2.addWidget(self.navbar)


        self.verticalLayout_3.addWidget(self.widget_navbar)

        self.stream_video = QLabel(self.centralwidget)
        self.stream_video.setObjectName(u"stream_video")
        sizePolicy.setHeightForWidth(self.stream_video.sizePolicy().hasHeightForWidth())
        self.stream_video.setSizePolicy(sizePolicy)
        self.stream_video.setStyleSheet(u"QLabel#stream_video{\n"
"    border: 3px solid rgb(0, 85, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.stream_video.setTextFormat(Qt.TextFormat.RichText)
        self.stream_video.setPixmap(QPixmap(u"statics/test_view.png"))
        self.stream_video.setScaledContents(False)
        self.stream_video.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.stream_video)

        self.widget_instruction = QWidget(self.centralwidget)
        self.widget_instruction.setObjectName(u"widget_instruction")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_instruction.sizePolicy().hasHeightForWidth())
        self.widget_instruction.setSizePolicy(sizePolicy1)
        self.widget_instruction.setMinimumSize(QSize(1347, 119))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_instruction)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_infomation = QLabel(self.widget_instruction)
        self.label_infomation.setObjectName(u"label_infomation")
        self.label_infomation.setMinimumSize(QSize(321, 81))
        self.label_infomation.setMaximumSize(QSize(436, 16777215))
        self.label_infomation.setStyleSheet(u"QLabel#label_infomation{\n"
"    background-color: rgb(226, 226, 226);\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"}")
        self.label_infomation.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_infomation.setWordWrap(False)

        self.horizontalLayout_3.addWidget(self.label_infomation)

        self.widget_instructions = QWidget(self.widget_instruction)
        self.widget_instructions.setObjectName(u"widget_instructions")
        self.widget_instructions.setMinimumSize(QSize(971, 101))
        self.widget_instructions.setStyleSheet(u"QWidget#widget_instructions  {\n"
"    background-color: rgb(226, 226, 226);\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_instructions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_instruction = QLabel(self.widget_instructions)
        self.label_instruction.setObjectName(u"label_instruction")
        self.label_instruction.setMinimumSize(QSize(111, 31))

        self.verticalLayout.addWidget(self.label_instruction)

        self.content_instruction = QLabel(self.widget_instructions)
        self.content_instruction.setObjectName(u"content_instruction")
        self.content_instruction.setMinimumSize(QSize(941, 41))
        self.content_instruction.setStyleSheet(u"QLabel#content_instruction{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: Black;\n"
"	border-radius: 6px;\n"
"}")

        self.verticalLayout.addWidget(self.content_instruction)


        self.horizontalLayout_3.addWidget(self.widget_instructions)


        self.verticalLayout_3.addWidget(self.widget_instruction)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1362, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.header_img.setText("")
        self.logo_img.setText("")
        self.Manual_Button.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.Instruction_Button.setText(QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.name_application.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Photobooth Stream</p></body></html>", None))
        self.Login_Button.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.stream_video.setText("")
        self.label_infomation.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Infomations</span></p></body></html>", None))
        self.label_instruction.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Instructions</span></p></body></html>", None))
        self.content_instruction.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Instruction for troubleshooting</p></body></html>", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

