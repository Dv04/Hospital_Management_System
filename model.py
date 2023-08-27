import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'Tesseract-OCR/tesseract.exe'

def ocr_core(filename):
    text = pytesseract.image_to_string(Image.open(filename))
    return text

