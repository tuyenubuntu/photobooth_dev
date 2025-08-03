from datetime import datetime
import os

def write_login_log(username, log_file, feature=""):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"[{now}] {username} | Login in: {feature}\n")

def log_action(user, action, log_path):
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    """Ghi log người dùng với hành động cụ thể."""
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | USER: {user} | ACTION: {action}\n")