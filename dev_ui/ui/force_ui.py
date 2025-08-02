# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'force.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(424, 256)
        Dialog.setMaximumSize(QSize(424, 256))
        self.label_forcewindow = QLabel(Dialog)
        self.label_forcewindow.setObjectName(u"label_forcewindow")
        self.label_forcewindow.setGeometry(QRect(-190, 0, 811, 61))
        font = QFont()
        font.setBold(False)
        self.label_forcewindow.setFont(font)
        self.label_forcewindow.setStyleSheet(u"QLabel#label_forcewindow{\n"
"    border: 2px solid black;\n"
"    border-radius: 4px;\n"
"    padding: 4px;\n"
"}\n"
"")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 70, 421, 48))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.label_force_laser = QLabel(self.widget)
        self.label_force_laser.setObjectName(u"label_force_laser")
        self.label_force_laser.setMaximumSize(QSize(291, 28))

        self.horizontalLayout.addWidget(self.label_force_laser)

        self.button_force_laser = QPushButton(self.widget)
        self.button_force_laser.setObjectName(u"button_force_laser")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_force_laser.sizePolicy().hasHeightForWidth())
        self.button_force_laser.setSizePolicy(sizePolicy)
        self.button_force_laser.setMaximumSize(QSize(75, 24))
        self.button_force_laser.setStyleSheet(u"QPushButton#button_force_laser{\n"
"    background-color: rgb(77, 155, 232);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_force_laser)

        self.status_force_laser = QLabel(self.widget)
        self.status_force_laser.setObjectName(u"status_force_laser")
        self.status_force_laser.setMaximumSize(QSize(30, 30))
        self.status_force_laser.setStyleSheet(u"QLabel#status_force_laser {\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.status_force_laser)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 140, 421, 48))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_force_oil = QLabel(self.widget_2)
        self.label_force_oil.setObjectName(u"label_force_oil")
        self.label_force_oil.setMaximumSize(QSize(291, 28))

        self.horizontalLayout_2.addWidget(self.label_force_oil)

        self.button_force_oil = QPushButton(self.widget_2)
        self.button_force_oil.setObjectName(u"button_force_oil")
        sizePolicy.setHeightForWidth(self.button_force_oil.sizePolicy().hasHeightForWidth())
        self.button_force_oil.setSizePolicy(sizePolicy)
        self.button_force_oil.setMaximumSize(QSize(75, 24))
        self.button_force_oil.setStyleSheet(u"QPushButton#button_force_oil{\n"
"    background-color: rgb(77, 155, 232);\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.button_force_oil)

        self.status_force_oil = QLabel(self.widget_2)
        self.status_force_oil.setObjectName(u"status_force_oil")
        self.status_force_oil.setMaximumSize(QSize(30, 30))
        self.status_force_oil.setStyleSheet(u"QLabel#status_force_oil{\n"
"    background-color: rgb(255, 0, 0);\n"
"    border-radius: 15px;\n"
"}\n"
"")

        self.horizontalLayout_2.addWidget(self.status_force_oil)

        self.button_force_cancel = QPushButton(Dialog)
        self.button_force_cancel.setObjectName(u"button_force_cancel")
        self.button_force_cancel.setGeometry(QRect(330, 230, 71, 24))
        sizePolicy.setHeightForWidth(self.button_force_cancel.sizePolicy().hasHeightForWidth())
        self.button_force_cancel.setSizePolicy(sizePolicy)
        self.button_force_cancel.setMaximumSize(QSize(75, 24))
        self.button_force_cancel.setStyleSheet(u"QPushButton#button_force_cancel{\n"
"    background-color: rgb(211, 211, 211);\n"
"}\n"
"")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_forcewindow.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Force Setting</span></p></body></html>", None))
        self.label_force_laser.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">Developing...</span></p></body></html>", None))
        self.button_force_laser.setText(QCoreApplication.translate("Dialog", u"Set", None))
        self.status_force_laser.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.label_force_oil.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:16pt;\">Developing...</span></p><p><br/></p></body></html>", None))
        self.button_force_oil.setText(QCoreApplication.translate("Dialog", u"Set", None))
        self.status_force_oil.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><br/></p></body></html>", None))
        self.button_force_cancel.setText(QCoreApplication.translate("Dialog", u"Logout", None))
    # retranslateUi

