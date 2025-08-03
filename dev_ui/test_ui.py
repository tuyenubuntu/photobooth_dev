import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class MyWindow:
    def __init__(self):
        loader = QUiLoader()
        ui_file = QFile("ui/control_panel.ui")
        ui_file.open(QFile.ReadOnly)
        self.window = loader.load(ui_file)
        ui_file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.window.show()
    sys.exit(app.exec())
