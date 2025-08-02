# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setWindowModality(Qt.WindowModality.WindowModal)
        Login.resize(367, 206)
        self.button_login = QDialogButtonBox(Login)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setGeometry(QRect(0, 160, 341, 32))
        self.button_login.setOrientation(Qt.Orientation.Horizontal)
        self.button_login.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label_passworlds = QLabel(Login)
        self.label_passworlds.setObjectName(u"label_passworlds")
        self.label_passworlds.setGeometry(QRect(30, 90, 91, 31))
        self.label_passworlds.setStyleSheet(u"QLabel#label_passworlds{\n"
"    background-color: rgb(0, 170, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.label_passworlds.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_passworlds = QLineEdit(Login)
        self.lineEdit_passworlds.setObjectName(u"lineEdit_passworlds")
        self.lineEdit_passworlds.setGeometry(QRect(140, 80, 201, 41))
        self.label_user = QLabel(Login)
        self.label_user.setObjectName(u"label_user")
        self.label_user.setGeometry(QRect(30, 40, 91, 31))
        self.label_user.setStyleSheet(u"QLabel#label_user{\n"
"    background-color: rgb(0, 170, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.label_user.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit_user = QLineEdit(Login)
        self.lineEdit_user.setObjectName(u"lineEdit_user")
        self.lineEdit_user.setGeometry(QRect(140, 30, 211, 41))

        self.retranslateUi(Login)
        self.button_login.accepted.connect(Login.accept)
        self.button_login.rejected.connect(Login.reject)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label_passworlds.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Passworls</span></p></body></html>", None))
        self.lineEdit_passworlds.setText("")
        self.lineEdit_passworlds.setPlaceholderText(QCoreApplication.translate("Login", u"Input Passworlds", None))
        self.label_user.setText(QCoreApplication.translate("Login", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">User</span></p></body></html>", None))
        self.lineEdit_user.setInputMask("")
        self.lineEdit_user.setText("")
        self.lineEdit_user.setPlaceholderText(QCoreApplication.translate("Login", u"Input User name", None))
    # retranslateUi

