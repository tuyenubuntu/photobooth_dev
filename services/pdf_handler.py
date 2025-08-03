import fitz  # PyMuPDF
from PySide6.QtGui import QImage, QPixmap
from config.settings import DPI_RENDER

def render_pdf_page(pdf_path, page_index, dpi=DPI_RENDER["dpi"]):
    doc = fitz.open(pdf_path)
    if page_index >= len(doc):
        return None, len(doc)

    page = doc.load_page(page_index)
    pix = page.get_pixmap(dpi=dpi)
    mode = QImage.Format_RGBA8888 if pix.alpha else QImage.Format_RGB888
    image = QImage(pix.samples, pix.width, pix.height, pix.stride, mode)
    pixmap = QPixmap.fromImage(image)
    return pixmap, len(doc)


def close_pdf(doc):
    if doc:
        doc.close()
