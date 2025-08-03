import os
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QToolButton, QAbstractButton
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from services.pdf_handler import render_pdf_page
from config.settings import UI_FILES

class InstructionDialog(QWidget):
    def __init__(self, username, pdf_path, table_window, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("ui/images/aiicon.png"))
        self.username = username
        self.pdf_path = pdf_path
        self.table_window = table_window

        loader = QUiLoader()
        file = QFile(UI_FILES["instruction"])
        if not file.open(QFile.ReadOnly):
            raise Exception("Không thể mở instruction.ui")

        self.ui = loader.load(file, self)
        file.close()

        if not self.ui:
            raise Exception("Không load được instruction.ui")

        self.setWindowTitle("Instruction PDF Viewer")
        self.ui.setWindowFlags(Qt.Window)

        self.label_pdf = self.ui.findChild(QLabel, "label_pdf_view")
        self.label_doc_name = self.ui.findChild(QLabel, "label_document_name")
        self.button_next = self.ui.findChild(QToolButton, "button_next")
        self.button_prev = self.ui.findChild(QToolButton, "button_previous")
        self.button_back = self.ui.findChild(QPushButton, "button_back_document")
        self.button_refresh = self.ui.findChild(QPushButton, "button_refesh")

        self.current_page = 0
        self.total_pages = 0

        self.update_view()

        if self.button_next:
            self.button_next.clicked.connect(self.next_page)
        if self.button_prev:
            self.button_prev.clicked.connect(self.prev_page)
        if self.button_back:
            self.button_back.clicked.connect(self.go_back)
        if self.button_refresh:
            self.button_refresh.clicked.connect(self.update_view)

        self.ui.show()

    def update_view(self):
        pixmap, total = render_pdf_page(self.pdf_path, self.current_page)
        self.total_pages = total
        if not pixmap:
            return

        self.label_pdf.setPixmap(pixmap.scaled(self.label_pdf.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        if self.label_doc_name:
            self.label_doc_name.setText(f"{os.path.basename(self.pdf_path)} - Page {self.current_page + 1}/{self.total_pages}")

    def next_page(self):
        if self.current_page + 1 < self.total_pages:
            self.current_page += 1
            self.update_view()

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.update_view()

    def go_back(self):
        self.ui.close()
        self.table_window.ui.show()
