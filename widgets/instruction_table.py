from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QIcon
from widgets.instruction_dialog import InstructionDialog
from config.settings import UI_FILES, DOCUMENTS


class InstructionTable(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        self.setWindowIcon(QIcon("ui/images/aiicon.png"))
        self.username = username
        loader = QUiLoader()
        file = QFile(UI_FILES["instruction_table"])
        if not file.open(QFile.ReadOnly):
            raise Exception("Can not open instruction_table.ui")

        self.ui = loader.load(file, self)
        file.close()

        if not self.ui:
            raise Exception("Unable to load instruction_table.ui")

        self.setWindowTitle("Instruction Table")
        self.ui.setWindowFlags(Qt.Window)

        # Assign button
        self.button_overview = self.ui.findChild(QPushButton, "button_overview")
        self.button_electric = self.ui.findChild(QPushButton, "button_edrawing")
        self.button_mechanical = self.ui.findChild(QPushButton, "button_mdrawing")

        if self.button_overview:
            self.button_overview.clicked.connect(lambda: self.open_instruction(DOCUMENTS["overview"]))
        if self.button_electric:
            self.button_electric.clicked.connect(lambda: self.open_instruction(DOCUMENTS["electric"]))
        if self.button_mechanical:
            self.button_mechanical.clicked.connect(lambda: self.open_instruction(DOCUMENTS["mechanical"]))
        # Assign button
        
        self.ui.show()

    def open_instruction(self, pdf_path):
        self.ui.hide()
        self.instruction_window = InstructionDialog(self.username, pdf_path, self)
