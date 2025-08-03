import os
import xml.etree.ElementTree as ET
from PySide6.QtWidgets import QLabel

def load_ordered_mappings(xml_path):
    """Load PLC mappings in order of appearance."""
    mappings = []
    if not os.path.exists(xml_path):
        print(f"[⚠️] Không tìm thấy file cấu hình: {xml_path}")
        return mappings

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        plc_mappings = root.find("PLC_mappings")
        if plc_mappings is None:
            print("[⚠️] Không tìm thấy thẻ PLC_mappings trong XML.")
            return mappings

        for mapping in plc_mappings.findall("mapping"):
            function = mapping.get("function", "").strip()
            address = mapping.get("address", "").strip()
            if function and address:
                mappings.append((function, address))
    except Exception as e:
        print(f"[❌] Lỗi khi đọc XML: {e}")
    return mappings


def apply_labels_from_config(widget, label_name_list, xml_path):
    mappings = load_ordered_mappings(xml_path)
    if not mappings:
        print("[⚠️] Không có dữ liệu mappings nào được load từ XML.")
        return

    for idx, label_name in enumerate(label_name_list):
        label_widget = widget.findChild(QLabel, label_name)
        if not label_widget:
            print(f"[❌] Không tìm thấy QLabel tên '{label_name}' trong giao diện")
            continue

        if idx >= len(mappings):
            print(f"[⚠️] Không đủ dữ liệu trong XML cho label '{label_name}' (index {idx})")
            continue
        function, address = mappings[idx]
        label_widget.setText(f"{function} ({address})")

def apply_flowline_name_from_config(widget, xml_path):
    """Cập nhật label flowline_name từ LINE_NAME trong XML"""
    if not os.path.exists(xml_path):
        print(f"[⚠️] Không tìm thấy file cấu hình: {xml_path}")
        return

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        line_name_elem = root.find("LINE_NAME")
        if line_name_elem is not None and line_name_elem.text:
            flowline_number = line_name_elem.text.strip()
            label = widget.findChild(QLabel, "flowline_name")
            if label:
                label.setText(f"Flowline {flowline_number}")
            else:
                print("[⚠️] Không tìm thấy QLabel tên 'flowline_name'")
        else:
            print("[⚠️] Không tìm thấy thẻ LINE_NAME hoặc nội dung trống")
    except Exception as e:
        print(f"[❌] Lỗi khi đọc LINE_NAME từ XML: {e}")

