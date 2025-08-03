from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from config.settings import UI_FILES


class ConfirmDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        file = QFile(UI_FILES["confirm"])
        if not file.open(QFile.ReadOnly):
            raise Exception("Không thể mở confirm.ui")

        self.ui = loader.load(file, self)
        file.close()

        if not self.ui:
            raise Exception("Không load được confirm.ui")

        self.setWindowTitle("confirm Window")
        self.ui.setWindowFlags(Qt.Window)
        self.ui.show()
