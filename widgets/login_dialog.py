from PySide6.QtWidgets import QLineEdit, QMessageBox, QDialogButtonBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from config.settings import UI_FILES, PASSWORD
from utils.helpers import is_correct_password, is_valid_username


class LoginDialog:
    def __init__(self, parent=None):
        loader = QUiLoader()
        file = QFile(UI_FILES["login"])
        if not file.open(QFile.ReadOnly):
            raise Exception("Không thể mở login.ui")

        self.dialog = loader.load(file, parent)
        file.close()

        if not self.dialog:
            raise Exception("Không load được login.ui")

        self.username_input = self.dialog.findChild(QLineEdit, "lineEdit_user")
        self.password_input = self.dialog.findChild(QLineEdit, "lineEdit_passworlds")
        self.button_box = self.dialog.findChild(QDialogButtonBox, "button_login")

        if self.password_input:
            self.password_input.setEchoMode(QLineEdit.Password)

        if self.button_box:
            self.button_box.accepted.connect(self.handle_login)
            self.button_box.rejected.connect(self.dialog.reject)

        self.login_success = False
        self.username = ""

    def exec(self):
        return self.dialog.exec()

    def handle_login(self):
        username = self.username_input.text().strip()
        password = self.password_input.text().strip()

        if not is_valid_username(username):
            QMessageBox.warning(self.dialog, "Missing information", "Input User name, please.")
            return

        if not is_correct_password(password, PASSWORD):
            QMessageBox.critical(self.dialog, "Sai mật khẩu", "Mật khẩu không chính xác.")
            return

        self.login_success = True
        self.username = username
        self.dialog.accept()
