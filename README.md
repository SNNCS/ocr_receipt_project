# Maybank ATM Receipt OCR

This project uses Tesseract OCR to extract deposit amount from a scanned Maybank ATM receipt image.

---

## Task Objective

Extract the **deposit amount** from a sample ATM receipt image using **computer vision** techniques.

---

## Approach

1. Load the receipt image using OpenCV
2. Convert it to grayscale and apply binary thresholding
3. Use Tesseract OCR to extract the text
4. Use regular expression to find the `RMxx.xx` amount string

---

## Technologies Used

- Python 3.12
- OpenCV (`cv2`)
- Tesseract OCR
- `pytesseract`
- `re` (regular expressions)
