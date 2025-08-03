# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'instruction.ui'
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
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(884, 811)
        Dialog.setMinimumSize(QSize(884, 811))
        icon = QIcon()
        icon.addFile(u"images/aiicon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(861, 59))
        self.widget.setMaximumSize(QSize(16777215, 59))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_back_document = QPushButton(self.widget)
        self.button_back_document.setObjectName(u"button_back_document")
        self.button_back_document.setMinimumSize(QSize(71, 41))
        self.button_back_document.setMaximumSize(QSize(71, 41))

        self.horizontalLayout.addWidget(self.button_back_document)

        self.label_document_name = QLabel(self.widget)
        self.label_document_name.setObjectName(u"label_document_name")
        self.label_document_name.setMinimumSize(QSize(331, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_document_name.setFont(font)
        self.label_document_name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_document_name)

        self.button_refesh = QPushButton(self.widget)
        self.button_refesh.setObjectName(u"button_refesh")
        self.button_refesh.setMinimumSize(QSize(61, 41))
        self.button_refesh.setMaximumSize(QSize(61, 41))
        self.button_refesh.setAutoDefault(False)

        self.horizontalLayout.addWidget(self.button_refesh)


        self.verticalLayout.addWidget(self.widget)

        self.widget_pdf_view = QWidget(Dialog)
        self.widget_pdf_view.setObjectName(u"widget_pdf_view")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_pdf_view.sizePolicy().hasHeightForWidth())
        self.widget_pdf_view.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.widget_pdf_view)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_pdf_view = QLabel(self.widget_pdf_view)
        self.label_pdf_view.setObjectName(u"label_pdf_view")
        sizePolicy.setHeightForWidth(self.label_pdf_view.sizePolicy().hasHeightForWidth())
        self.label_pdf_view.setSizePolicy(sizePolicy)
        self.label_pdf_view.setScaledContents(True)
        self.label_pdf_view.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout_2.addWidget(self.label_pdf_view)


        self.verticalLayout.addWidget(self.widget_pdf_view)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(891, 49))
        self.widget_2.setMaximumSize(QSize(16777215, 49))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_previous = QToolButton(self.widget_2)
        self.button_previous.setObjectName(u"button_previous")
        self.button_previous.setMinimumSize(QSize(41, 31))
        self.button_previous.setMaximumSize(QSize(41, 31))
        self.button_previous.setText(u"")
        icon1 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoPrevious))
        self.button_previous.setIcon(icon1)
        self.button_previous.setPopupMode(QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.button_previous.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.button_previous.setArrowType(Qt.ArrowType.LeftArrow)

        self.horizontalLayout_2.addWidget(self.button_previous)

        self.button_next = QToolButton(self.widget_2)
        self.button_next.setObjectName(u"button_next")
        self.button_next.setMinimumSize(QSize(41, 31))
        self.button_next.setMaximumSize(QSize(41, 31))
        icon2 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.GoNext))
        self.button_next.setIcon(icon2)
        self.button_next.setArrowType(Qt.ArrowType.RightArrow)

        self.horizontalLayout_2.addWidget(self.button_next)


        self.verticalLayout.addWidget(self.widget_2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Documentation", None))
        self.button_back_document.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.label_document_name.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">TextLabel</span></p></body></html>", None))
        self.button_refesh.setText(QCoreApplication.translate("Dialog", u"Refesh", None))
        self.label_pdf_view.setText(QCoreApplication.translate("Dialog", u"PDF", None))
        self.button_next.setText("")
    # retranslateUi

