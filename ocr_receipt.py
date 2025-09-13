import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image = cv2.imread("maybank_atm_receipt.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

text = pytesseract.image_to_string(thresh)

match = re.search(r"RM\s?(\d+\.\d{2})", text)
if match:
    print("Detected Deposit Amount:", match.group(0))
else:
    print("Deposit amount not found.")
