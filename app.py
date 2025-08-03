import sys
import os
import cv2
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QLabel, QMessageBox, QLineEdit, QDialogButtonBox, QPushButton, QWidget
)
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QPainter, QPainterPath


class LoginDialog:
    def __init__(self, parent=None):
        loader = QUiLoader()
        file = QFile("login.ui")
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
        if not username:
            QMessageBox.warning(self.dialog, "Missing information", "Please enter a username.")
            return
        if password != "adlink":
            QMessageBox.critical(self.dialog, "Incorrect password", "Incorrect password.")
            return
        self.login_success = True
        self.username = username
        self.dialog.accept()


class ForceDialog(QWidget):
    def __init__(self, username, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        file = QFile("force.ui")
        if not file.open(QFile.ReadOnly):
            raise Exception("Không thể mở force.ui")
        self.ui = loader.load(file, self)
        file.close()
        if not self.ui:
            raise Exception("Không load được force.ui")

        self.setWindowTitle("Force Control")
        self.ui.setWindowFlags(Qt.Window)
        self.username = username

        self.cancel_button = self.ui.findChild(QPushButton, "button_force_cancel")
        if self.cancel_button:
            self.cancel_button.clicked.connect(self.handle_cancel)

        self.ui.show()

    def handle_cancel(self):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{now} | USER: {self.username} | ACTION: Cancelled Force Window\n"
        with open("login_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line)
        self.ui.close()


class MainApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.capture_image = None
        self.stream_active = False

        loader = QUiLoader()
        ui_file = QFile("main.ui")
        if not ui_file.open(QFile.ReadOnly):
            raise Exception("Không thể mở main.ui")
        self.window = loader.load(ui_file)
        ui_file.close()

        self.label = self.window.findChild(QLabel, "stream_video")
        self.info_label = self.window.findChild(QLabel, "content_instruction")
        self.login_button = self.window.findChild(QPushButton, "Login_Button")
        self.manual_button = self.window.findChild(QPushButton, "Manual_Button")
        self.instruction_button = self.window.findChild(QPushButton, "Instruction_Button")
        self.activate_button = self.window.findChild(QPushButton, "button_activate")
        self.capture_button = self.window.findChild(QPushButton, "button_capture")

        if self.login_button:
            self.login_button.clicked.connect(self.open_login)
        if self.manual_button:
            self.manual_button.clicked.connect(self.open_manual_login)
        if self.instruction_button:
            self.instruction_button.clicked.connect(self.open_instruction_login)
        if self.activate_button:
            self.activate_button.clicked.connect(self.toggle_stream)
        if self.capture_button:
            self.capture_button.clicked.connect(self.capture_frame)

        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

        self.window.show()
        sys.exit(self.app.exec())

    def log_info(self, text):
        now = datetime.now().strftime("%H:%M:%S")
        log = f"[{now}] {text}"
        if self.info_label:
            self.info_label.setText(log)

    def toggle_stream(self):
        self.stream_active = not self.stream_active
        if self.stream_active:
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.log_info("Camera không mở được.")
                return
            self.timer.start(30)
            self.activate_button.setText("Deactivate")
            self.log_info("Camera đã kích hoạt.")
        else:
            self.timer.stop()
            self.activate_button.setText("Activate")
            if self.cap:
                self.cap.release()
                self.cap = None
            if os.path.exists(r"statics\test_view.png"):
                pix = QPixmap(r"statics\test_view.png")
            else:
                pix = QPixmap(self.label.size())
                pix.fill(Qt.gray)
            self.label.setPixmap(pix.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.log_info("Camera đã tắt.")

    def update_frame(self):
        if not self.stream_active or not self.cap:
            return
        ret, frame = self.cap.read()
        if not ret:
            return
        self.capture_image = frame.copy()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = frame.shape
        bytes_per_line = ch * w
        qimg = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimg)

        rounded = QPixmap(pixmap.size())
        rounded.fill(Qt.transparent)
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.Antialiasing)
        path = QPainterPath()
        path.addRoundedRect(0, 0, pixmap.width(), pixmap.height(), 10, 10)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        self.label.setPixmap(rounded.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def capture_frame(self):
        if self.capture_image is None:
            self.log_info("Camera chưa bật hoặc không có hình.")
            return
        if not os.path.exists("capture_images"):
            os.makedirs("capture_images")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capture_images/{timestamp}_ID.jpg"
        cv2.imwrite(filename, self.capture_image)
        self.log_info(f"Ảnh đã lưu: {filename}")

    def open_login(self):
        login = LoginDialog(self.window)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Login Mode")
            self.log_info(f"{login.username} đăng nhập (Login Mode)")
            QMessageBox.information(self.window, "Login", f"Hello {login.username}, You are in Login mode.")

    def open_manual_login(self):
        login = LoginDialog(self.window)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Manual Mode")
            self.log_info(f"{login.username} đăng nhập Manual")
            ForceDialog(login.username, self.window)

    def open_instruction_login(self):
        login = LoginDialog(self.window)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Instruction Mode")
            self.log_info(f"{login.username} đăng nhập Instruction")
            QMessageBox.information(self.window, "Login", f"Hello {login.username}, Instruction feature under development.")

    def log_login(self, username, feature_used):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{now} | USER: {username} | FEATURE: {feature_used}\n"
        with open("login_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line)

    def __del__(self):
        if hasattr(self, 'cap') and self.cap and self.cap.isOpened():
            self.cap.release()


if __name__ == "__main__":
    MainApp()