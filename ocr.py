import easyocr
import cv2


def ocr(IMAGE_PATH):
    img = cv2.imread(IMAGE_PATH)
    #img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    spacer = 100

    reader = easyocr.Reader(['en'])
    # Preprocessing image
    img = cv2.bilateralFilter(img, 9, 75, 75)
    #thread, img = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

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
