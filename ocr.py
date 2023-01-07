import easyocr
import cv2


def ocr(img):
    spacer = 100

    reader = easyocr.Reader(['en'])
    # Preprocessing image
    img = cv2.bilateralFilter(img, 9, 75, 75)

    text = None
    result = reader.readtext(img)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for detection in result:
        top_left = tuple(detection[0][0])
        bottom_right = tuple(detection[0][2])
        text = detection[1]
        img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 3)
        img = cv2.putText(img, text, (20, spacer), font,
                          0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15
    return text
