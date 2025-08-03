# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flowlines.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1374, 884)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1374, 884))
        icon = QIcon()
        icon.addFile(u"ui/images/aiicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QPushButton#Main_Button {\n"
"    background-color: rgb(80, 159, 239);\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1314, 818))
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.widget_navbar = QWidget(self.centralwidget)
        self.widget_navbar.setObjectName(u"widget_navbar")
        sizePolicy.setHeightForWidth(self.widget_navbar.sizePolicy().hasHeightForWidth())
        self.widget_navbar.setSizePolicy(sizePolicy)
        self.widget_navbar.setMinimumSize(QSize(0, 61))
        self.widget_navbar.setMaximumSize(QSize(16777215, 61))
        self.verticalLayout_2 = QVBoxLayout(self.widget_navbar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_img = QLabel(self.widget_navbar)
        self.header_img.setObjectName(u"header_img")
        sizePolicy.setHeightForWidth(self.header_img.sizePolicy().hasHeightForWidth())
        self.header_img.setSizePolicy(sizePolicy)
        self.header_img.setMinimumSize(QSize(0, 16))
        self.header_img.setMaximumSize(QSize(16777215, 16))
        self.header_img.setPixmap(QPixmap(u"ui/images/header.png"))
        self.header_img.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.header_img, 0, Qt.AlignmentFlag.AlignTop)

        self.navbar = QWidget(self.widget_navbar)
        self.navbar.setObjectName(u"navbar")
        sizePolicy.setHeightForWidth(self.navbar.sizePolicy().hasHeightForWidth())
        self.navbar.setSizePolicy(sizePolicy)
        self.navbar.setMinimumSize(QSize(0, 45))
        self.navbar.setMaximumSize(QSize(16777215, 51))
        self.navbar.setAutoFillBackground(False)
        self.navbar.setStyleSheet(u"QWidget#navbar {\n"
"    background-color: #1f2a44;  /* xanh \u0111en */\n"
"    color: white;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.navbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_img = QLabel(self.navbar)
        self.logo_img.setObjectName(u"logo_img")
        sizePolicy.setHeightForWidth(self.logo_img.sizePolicy().hasHeightForWidth())
        self.logo_img.setSizePolicy(sizePolicy)
        self.logo_img.setMinimumSize(QSize(141, 31))
        self.logo_img.setMaximumSize(QSize(141, 31))
        self.logo_img.setPixmap(QPixmap(u"ui/images/bosch_logo.png"))
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

        self.flowline_name = QLabel(self.navbar)
        self.flowline_name.setObjectName(u"flowline_name")
        sizePolicy.setHeightForWidth(self.flowline_name.sizePolicy().hasHeightForWidth())
        self.flowline_name.setSizePolicy(sizePolicy)
        self.flowline_name.setMinimumSize(QSize(725, 33))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setKerning(True)
        self.flowline_name.setFont(font)
        self.flowline_name.setStyleSheet(u"QLabel#flowline_name {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    qproperty-alignment: 'AlignCenter';\n"
"}\n"
"")
        self.flowline_name.setScaledContents(True)

        self.horizontalLayout.addWidget(self.flowline_name)

        self.name_app = QLabel(self.navbar)
        self.name_app.setObjectName(u"name_app")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name_app.sizePolicy().hasHeightForWidth())
        self.name_app.setSizePolicy(sizePolicy1)
        self.name_app.setMinimumSize(QSize(211, 31))
        self.name_app.setMaximumSize(QSize(211, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.name_app.setFont(font1)
        self.name_app.setStyleSheet(u"QLabel#name_app {\n"
"    color: white;\n"
"}")
        self.name_app.setScaledContents(True)

        self.horizontalLayout.addWidget(self.name_app)


        self.verticalLayout_2.addWidget(self.navbar)


        self.verticalLayout_3.addWidget(self.widget_navbar)

        self.stream_video = QLabel(self.centralwidget)
        self.stream_video.setObjectName(u"stream_video")
        sizePolicy.setHeightForWidth(self.stream_video.sizePolicy().hasHeightForWidth())
        self.stream_video.setSizePolicy(sizePolicy)
        self.stream_video.setStyleSheet(u"QLabel#stream_video{\n"
"    border: 1px solid rgb(0, 85, 255);\n"
"    border-radius: 20px;\n"
"}\n"
"")
        self.stream_video.setTextFormat(Qt.TextFormat.RichText)
        self.stream_video.setPixmap(QPixmap(u"ui/images/test_view.png"))
        self.stream_video.setScaledContents(True)
        self.stream_video.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.stream_video)

        self.IO_status = QWidget(self.centralwidget)
        self.IO_status.setObjectName(u"IO_status")
        self.IO_status.setEnabled(True)
        sizePolicy.setHeightForWidth(self.IO_status.sizePolicy().hasHeightForWidth())
        self.IO_status.setSizePolicy(sizePolicy)
        self.IO_status.setMinimumSize(QSize(0, 51))
        self.IO_status.setMaximumSize(QSize(16777215, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.IO_status)
        self.horizontalLayout_2.setSpacing(100)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_sent_to_laser = QWidget(self.IO_status)
        self.widget_sent_to_laser.setObjectName(u"widget_sent_to_laser")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_sent_to_laser.sizePolicy().hasHeightForWidth())
        self.widget_sent_to_laser.setSizePolicy(sizePolicy2)
        self.widget_sent_to_laser.setMinimumSize(QSize(271, 31))
        self.label_sent_to_laser = QLabel(self.widget_sent_to_laser)
        self.label_sent_to_laser.setObjectName(u"label_sent_to_laser")
        self.label_sent_to_laser.setGeometry(QRect(0, 0, 211, 31))
        self.label_sent_to_laser.setMinimumSize(QSize(211, 31))
        self.label_sent_to_laser.setScaledContents(True)
        self.status_sent_to_laser = QLabel(self.widget_sent_to_laser)
        self.status_sent_to_laser.setObjectName(u"status_sent_to_laser")
        self.status_sent_to_laser.setGeometry(QRect(220, 0, 30, 30))
        self.status_sent_to_laser.setMinimumSize(QSize(30, 30))
        self.status_sent_to_laser.setMaximumSize(QSize(30, 30))
        self.status_sent_to_laser.setStyleSheet(u"QLabel#status_sent_to_laser{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.widget_sent_to_laser)

        self.widget_sent_to_oildipping = QWidget(self.IO_status)
        self.widget_sent_to_oildipping.setObjectName(u"widget_sent_to_oildipping")
        sizePolicy2.setHeightForWidth(self.widget_sent_to_oildipping.sizePolicy().hasHeightForWidth())
        self.widget_sent_to_oildipping.setSizePolicy(sizePolicy2)
        self.widget_sent_to_oildipping.setMinimumSize(QSize(281, 31))
        self.label_sent_to_oil = QLabel(self.widget_sent_to_oildipping)
        self.label_sent_to_oil.setObjectName(u"label_sent_to_oil")
        self.label_sent_to_oil.setGeometry(QRect(10, 0, 221, 31))
        self.label_sent_to_oil.setMinimumSize(QSize(221, 31))
        self.label_sent_to_oil.setScaledContents(True)
        self.status_sent_to_oil = QLabel(self.widget_sent_to_oildipping)
        self.status_sent_to_oil.setObjectName(u"status_sent_to_oil")
        self.status_sent_to_oil.setGeometry(QRect(230, 0, 30, 30))
        self.status_sent_to_oil.setMinimumSize(QSize(30, 30))
        self.status_sent_to_oil.setMaximumSize(QSize(30, 30))
        self.status_sent_to_oil.setStyleSheet(u"QLabel#status_sent_to_oil{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.widget_sent_to_oildipping)

        self.widget_recieve_from_laser = QWidget(self.IO_status)
        self.widget_recieve_from_laser.setObjectName(u"widget_recieve_from_laser")
        sizePolicy2.setHeightForWidth(self.widget_recieve_from_laser.sizePolicy().hasHeightForWidth())
        self.widget_recieve_from_laser.setSizePolicy(sizePolicy2)
        self.widget_recieve_from_laser.setMinimumSize(QSize(291, 31))
        self.label_receive_from_laser = QLabel(self.widget_recieve_from_laser)
        self.label_receive_from_laser.setObjectName(u"label_receive_from_laser")
        self.label_receive_from_laser.setGeometry(QRect(10, 0, 231, 31))
        self.label_receive_from_laser.setMinimumSize(QSize(231, 31))
        self.label_receive_from_laser.setScaledContents(True)
        self.status_receive_laser = QLabel(self.widget_recieve_from_laser)
        self.status_receive_laser.setObjectName(u"status_receive_laser")
        self.status_receive_laser.setGeometry(QRect(250, 0, 30, 30))
        self.status_receive_laser.setMinimumSize(QSize(30, 30))
        self.status_receive_laser.setMaximumSize(QSize(30, 30))
        self.status_receive_laser.setStyleSheet(u"QLabel#status_receive_laser{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.widget_recieve_from_laser)

        self.widget_recieve_from_rework = QWidget(self.IO_status)
        self.widget_recieve_from_rework.setObjectName(u"widget_recieve_from_rework")
        sizePolicy2.setHeightForWidth(self.widget_recieve_from_rework.sizePolicy().hasHeightForWidth())
        self.widget_recieve_from_rework.setSizePolicy(sizePolicy2)
        self.widget_recieve_from_rework.setMinimumSize(QSize(271, 31))
        self.status_rework_key = QLabel(self.widget_recieve_from_rework)
        self.status_rework_key.setObjectName(u"status_rework_key")
        self.status_rework_key.setGeometry(QRect(220, 0, 30, 30))
        self.status_rework_key.setMinimumSize(QSize(30, 30))
        self.status_rework_key.setMaximumSize(QSize(30, 30))
        self.status_rework_key.setStyleSheet(u"QLabel#status_rework_key{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.label_rework = QLabel(self.widget_recieve_from_rework)
        self.label_rework.setObjectName(u"label_rework")
        self.label_rework.setGeometry(QRect(11, 0, 211, 31))
        self.label_rework.setMinimumSize(QSize(211, 31))
        self.label_rework.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.widget_recieve_from_rework)


        self.verticalLayout_3.addWidget(self.IO_status)

        self.widget_instruction = QWidget(self.centralwidget)
        self.widget_instruction.setObjectName(u"widget_instruction")
        self.widget_instruction.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.widget_instruction.sizePolicy().hasHeightForWidth())
        self.widget_instruction.setSizePolicy(sizePolicy1)
        self.widget_instruction.setMinimumSize(QSize(0, 119))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_instruction)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_infomation = QLabel(self.widget_instruction)
        self.label_infomation.setObjectName(u"label_infomation")
        self.label_infomation.setMinimumSize(QSize(231, 0))
        self.label_infomation.setMaximumSize(QSize(321, 16777215))
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
        self.widget_instructions.setMinimumSize(QSize(841, 0))
        self.widget_instructions.setStyleSheet(u"QWidget#widget_instructions  {\n"
"    background-color: rgb(226, 226, 226);\n"
"    color: black;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget_instructions)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_instruction = QLabel(self.widget_instructions)
        self.label_instruction.setObjectName(u"label_instruction")

        self.verticalLayout.addWidget(self.label_instruction)

        self.content_instruction = QLabel(self.widget_instructions)
        self.content_instruction.setObjectName(u"content_instruction")
        self.content_instruction.setStyleSheet(u"QLabel#content_instruction{\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: Black;\n"
"	border-radius: 6px;\n"
"}")

        self.verticalLayout.addWidget(self.content_instruction)


        self.horizontalLayout_3.addWidget(self.widget_instructions)

        self.button_confirm = QPushButton(self.widget_instruction)
        self.button_confirm.setObjectName(u"button_confirm")
        self.button_confirm.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.button_confirm.sizePolicy().hasHeightForWidth())
        self.button_confirm.setSizePolicy(sizePolicy3)
        self.button_confirm.setMinimumSize(QSize(141, 41))
        self.button_confirm.setMaximumSize(QSize(141, 41))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        self.button_confirm.setFont(font2)
        self.button_confirm.setStyleSheet(u"QPushButton#button_confirm {\n"
"    color: black;\n"
"    /* font-weight: bold; */\n"
"    background-color: rgb(0, 170, 255);\n"
"    text-align: center; /* Kh\u00f4ng ch\u00ednh th\u1ee9c h\u1ed7 tr\u1ee3 nh\u01b0ng \u0111\u1ec3 m\u00f4 t\u1ea3 \u00fd \u0111\u1ecbnh */\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.button_confirm)


        self.verticalLayout_3.addWidget(self.widget_instruction)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1374, 33))
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI Camera Flowline", None))
        self.header_img.setText("")
        self.logo_img.setText("")
        self.Manual_Button.setText(QCoreApplication.translate("MainWindow", u"Manual Mode", None))
        self.Instruction_Button.setText(QCoreApplication.translate("MainWindow", u"Instruction", None))
        self.flowline_name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Flowline 07</p></body></html>", None))
        self.name_app.setText(QCoreApplication.translate("MainWindow", u"HcP/MSE3 AI Flowline System", None))
        self.stream_video.setText("")
        self.label_sent_to_laser.setText(QCoreApplication.translate("MainWindow", u"Belt on scale sent to laser (I3.2)", None))
        self.status_sent_to_laser.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_sent_to_oil.setText(QCoreApplication.translate("MainWindow", u"Sent to oildipping machine (I7.3)", None))
        self.status_sent_to_oil.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_receive_from_laser.setText(QCoreApplication.translate("MainWindow", u"Recieve from laser machine (Q3.3)", None))
        self.status_receive_laser.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
        self.status_rework_key.setText("")
        self.label_rework.setText(QCoreApplication.translate("MainWindow", u"Receive from key rework (NO)", None))
        self.label_infomation.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Infomations</span></p></body></html>", None))
        self.label_instruction.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Instructions</span></p></body></html>", None))
        self.content_instruction.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Instruction for troubleshooting</p></body></html>", None))
        self.button_confirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

