import sys
import os
import cv2
from datetime import datetime
from PySide6.QtCore import QTimer, Qt, QFile, QCoreApplication
from PySide6.QtWidgets import QLabel, QPushButton, QWidget, QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QPixmap

from widgets.login_dialog import LoginDialog
from widgets.instruction_table import InstructionTable
from widgets.force_dialog import ForceDialog
from widgets.confirm_dialog import ConfirmDialog
from config.settings import UI_FILES, LOG, PASSWORD, CONFIG_FILE
from services.video_stream import get_rounded_frame
from services.logger import log_action
from services.process_config import apply_labels_from_config, apply_flowline_name_from_config


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon("ui/images/aiicon.png"))

        # Load UI từ file .ui
        loader = QUiLoader()
        ui_file = QFile(UI_FILES["main"])
        if not ui_file.open(QFile.ReadOnly):
            raise Exception("Không thể mở flowlines.ui")
        loaded_ui = loader.load(ui_file, self)
        ui_file.close()
        if not loaded_ui:
            raise Exception("Không load được flowlines.ui")
        layout = loaded_ui.layout()
        if layout:
            self.setLayout(layout)

        ######### Stream Video ##########
        self.label = self.findChild(QLabel, "stream_video")
        if not self.label:
            raise Exception("Không tìm thấy QLabel tên 'stream_video' trong flowlines.ui")

        # Camera & Timer
        self.cap = None
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.stream_active = False
        self.capture_image = None
        ######### Stream Video ##########

        ######### Gán nút ##########
        self.login_button = self.findChild(QPushButton, "Login_Button")
        self.manual_button = self.findChild(QPushButton, "Manual_Button")
        self.instruction_button = self.findChild(QPushButton, "Instruction_Button")
        self.activate_button = self.findChild(QPushButton, "button_activate")
        self.capture_button = self.findChild(QPushButton, "button_capture")

        self.user_label = self.findChild(QLabel, "label_user")
        self.info_label = self.findChild(QLabel, "content_instruction")

        # Kết nối nút
        if self.login_button:
            self.login_button.clicked.connect(self.open_login)
        if self.manual_button:
            self.manual_button.clicked.connect(self.open_force_login)
        if self.instruction_button:
            self.instruction_button.clicked.connect(self.open_instruction_login)
        if self.activate_button:
            self.activate_button.clicked.connect(self.toggle_stream)
        if self.capture_button:
            self.capture_button.clicked.connect(self.capture_frame)
        ######### Gán nút ##########

    # ----------- Stream logic ----------
    def toggle_stream(self):
        """Bật/Tắt camera"""
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
            # Hiển thị ảnh mặc định khi tắt camera
            if os.path.exists(r"statics\test_view.png"):
                pix = QPixmap(r"statics\test_view.png")
            else:
                pix = QPixmap(self.label.size())
                pix.fill(Qt.gray)
            self.label.setPixmap(pix.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.log_info("Camera đã tắt.")

    def update_frame(self):
        """Cập nhật frame video"""
        if not self.stream_active or not self.cap:
            return
        ret, frame = self.cap.read()
        if not ret:
            return
        self.capture_image = frame.copy()
        rounded = get_rounded_frame(self.cap)
        if rounded and self.label:
            self.label.setPixmap(rounded.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def capture_frame(self):
        """Chụp và lưu ảnh"""
        if self.capture_image is None:
            self.log_info("Camera chưa bật hoặc không có hình.")
            return
        if not os.path.exists("capture_images"):
            os.makedirs("capture_images")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"capture_images/{timestamp}_ID.jpg"
        cv2.imwrite(filename, self.capture_image)
        self.log_info(f"Ảnh đã lưu: {filename}")
    # ----------- Stream logic ----------

    # ----------- Login & Feature ----------
    def open_login(self):
        login = LoginDialog(self)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Login Mode")
            self.log_info(f"{login.username} đăng nhập (Login Mode)")
            QMessageBox.information(self, "Login", f"Hello {login.username}, You are in Login mode.")
            if self.user_label:
                self.user_label.setText(login.username)

    def open_force_login(self):
        login = LoginDialog(self)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Manual Mode")
            self.log_info(f"{login.username} đăng nhập Manual")
            if self.user_label:
                self.user_label.setText(login.username)
            self.force_window = ForceDialog(self)

    def open_instruction_login(self):
        login = LoginDialog(self)
        if login.exec() and login.login_success:
            self.log_login(login.username, "Instruction Mode")
            self.log_info(f"{login.username} đăng nhập Instruction")
            QMessageBox.information(self, "Login", f"Hello {login.username}, Instruction feature under development.")
            if self.user_label:
                self.user_label.setText(login.username)
    # ----------- Login & Feature ----------

    # ----------- Helper ----------
    def log_info(self, text):
        now = datetime.now().strftime("%H:%M:%S")
        log = f"[{now}] {text}"
        if self.info_label:
            self.info_label.setText(log)

    def log_login(self, username, feature_used):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{now} | USER: {username} | FEATURE: {feature_used}\n"
        with open("login_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line)
    # ----------- Helper ----------

    def closeEvent(self, event):
        if hasattr(self, 'timer'):
            self.timer.stop()
        if hasattr(self, 'cap') and self.cap and self.cap.isOpened():
            self.cap.release()
        cv2.destroyAllWindows()
        QCoreApplication.quit()
        event.accept()
