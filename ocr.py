import easyocr
import cv2


def ocr(img):
    reader = easyocr.Reader(['en'])
    # Preprocessing image
    img = cv2.bilateralFilter(img, 9, 75, 75)

    text = None
    result = reader.readtext(img)
    for detection in result:
        text = detection[1]
    return text
