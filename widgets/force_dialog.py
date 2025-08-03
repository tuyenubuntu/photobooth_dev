from PySide6.QtWidgets import QWidget, QPushButton
from PySide6.QtCore import QFile, Qt
from PySide6.QtUiTools import QUiLoader
from config.settings import UI_FILES


class ForceDialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        loader = QUiLoader()
        file = QFile(UI_FILES["force"])
        if not file.open(QFile.ReadOnly):
            raise Exception("Không thể mở force.ui")

        self.ui = loader.load(file, self)
        file.close()

        if not self.ui:
            raise Exception("Không load được force.ui")

        self.setWindowTitle("Force Window")
        self.ui.setWindowFlags(Qt.Window)

        cancel_btn = self.ui.findChild(QPushButton, "button_force_cancel")
        if cancel_btn:
            cancel_btn.clicked.connect(self.ui.close)

        self.ui.show()
