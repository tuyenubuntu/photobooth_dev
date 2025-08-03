from datetime import datetime
from config.settings import PASSWORD
def is_valid_username(username):
    """Kiểm tra username hợp lệ."""
    return bool(username and username.strip())

def is_correct_password(password, expected):
    """Kiểm tra mật khẩu có khớp không."""
    expected = PASSWORD["feature"]
    return password == expected
