# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instruction_table.ui'
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
        Dialog.resize(655, 364)
        Dialog.setMinimumSize(QSize(655, 364))
        Dialog.setMaximumSize(QSize(655, 364))
        icon = QIcon()
        icon.addFile(u"images/aiicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 90, 647, 79))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_overview = QPushButton(self.widget)
        self.button_overview.setObjectName(u"button_overview")
        self.button_overview.setMinimumSize(QSize(121, 61))

        self.horizontalLayout.addWidget(self.button_overview)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(121, 61))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(121, 61))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(121, 61))

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(121, 61))

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 170, 647, 79))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_edrawing = QPushButton(self.widget_2)
        self.button_edrawing.setObjectName(u"button_edrawing")
        self.button_edrawing.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_2.addWidget(self.button_edrawing)

        self.button_mdrawing = QPushButton(self.widget_2)
        self.button_mdrawing.setObjectName(u"button_mdrawing")
        self.button_mdrawing.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_2.addWidget(self.button_mdrawing)

        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_2.addWidget(self.pushButton_8)

        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_9 = QPushButton(self.widget_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 250, 647, 79))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_reserve1 = QPushButton(self.widget_3)
        self.button_reserve1.setObjectName(u"button_reserve1")
        self.button_reserve1.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_3.addWidget(self.button_reserve1)

        self.button_reserve2 = QPushButton(self.widget_3)
        self.button_reserve2.setObjectName(u"button_reserve2")
        self.button_reserve2.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_3.addWidget(self.button_reserve2)

        self.button_reserve3 = QPushButton(self.widget_3)
        self.button_reserve3.setObjectName(u"button_reserve3")
        self.button_reserve3.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_3.addWidget(self.button_reserve3)

        self.button_reserve4 = QPushButton(self.widget_3)
        self.button_reserve4.setObjectName(u"button_reserve4")
        self.button_reserve4.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_3.addWidget(self.button_reserve4)

        self.button_reserve5 = QPushButton(self.widget_3)
        self.button_reserve5.setObjectName(u"button_reserve5")
        self.button_reserve5.setMinimumSize(QSize(121, 61))

        self.horizontalLayout_3.addWidget(self.button_reserve5)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 10, 181, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Control Panel Instruction", None))
        self.button_overview.setText(QCoreApplication.translate("Dialog", u"Overview", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"Setting", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"IP Camera", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Address PLC", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Stroubleshooting", None))
        self.button_edrawing.setText(QCoreApplication.translate("Dialog", u"E. Drawing", None))
        self.button_mdrawing.setText(QCoreApplication.translate("Dialog", u"M. Drawing", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"Part List", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"Update SW", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"Commit Version", None))
        self.button_reserve1.setText(QCoreApplication.translate("Dialog", u"Reserve", None))
        self.button_reserve2.setText(QCoreApplication.translate("Dialog", u"Reserve", None))
        self.button_reserve3.setText(QCoreApplication.translate("Dialog", u"Reserve", None))
        self.button_reserve4.setText(QCoreApplication.translate("Dialog", u"Reserve", None))
        self.button_reserve5.setText(QCoreApplication.translate("Dialog", u"Reserve", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Control Panel</span></p></body></html>", None))
    # retranslateUi

