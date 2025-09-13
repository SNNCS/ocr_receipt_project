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

## How To Run
### 1. Install dependencies:

```pip install opencv-python pytesseract```

### 2.Make sure Tesseract is installed and configured:

```
# In main.py
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

### 3. Run the script:

python main.py


Expected output:

```
Detected Deposit Amount: RM25.00
```
