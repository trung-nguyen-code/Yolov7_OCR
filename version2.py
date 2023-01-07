# import os
# import threading
#
# import cv2
# import pytesseract
# import requests
# import queue
# from detect import detect_export
# from ocr import ocr
# print_lock = threading.Lock()
#
# pytesseract.pytesseract.tesseract_cmd = r'D:\Yolov7_OCR\yolov7\tesseract.exe'
#
# def send_data(img, action,vehicleCode):
#     files = {
#         'file': (img, open(img, 'rb'), 'image/jpg')
#     }
#     data = {
#         'vehicleCode': vehicleCode
#     }
#
#     url_api = 'https://8cc5-171-241-50-107.ap.ngrok.io/api/v1/data/' + action
#     res = requests.post(url_api, files = files, data = data)
#     try:
#         data = res.json()
#         status_code = res.status_code
#         print('response data:', data, ', status code:', status_code)
#     except requests.exceptions.RequestException:
#         print('response text:', res.text)
#
#
# def read_string():
#     directory = "runs\detect\exp"
#     impath = os.path.join(directory, 'bsxot.jpg')
#     print(impath)
#     img_cv = cv2.imread(impath)
#     img_gray = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
#
#     img_gray = cv2.bilateralFilter(img_gray, 11, 17, 17)
#     edged = cv2.Canny(img_gray, 190, 200)
#     contours, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#
#     contours = sorted(contours, key=cv2.contourArea, reverse=True)[:50]
#     contour_licence_plate = None
#
#
#     licence_plate = None
#     x = 0
#     y = 0
#     w = 0
#     h = 0
#     for contour in contours:
#         perimeter = cv2.arcLength(contour, True)
#         approx = cv2.approxPolyDP(contour, 0.018 * perimeter, True)
#         if len(approx) == 4:
#             contour_licence_plate = approx
#             x, y, w, h = cv2.boundingRect(contour_licence_plate)
#             # print(x, y, w, h)
#             licence_plate = img_gray[y:y + h, x:x + w]
#             break
#
#     thread, binaryimg = cv2.threshold(img_gray, 85, 255, cv2.THRESH_BINARY)
#     print(thread)
#     text = pytesseract.image_to_string(binaryimg, config='--oem 3 --psm 6')
#     #print(text)
#     #send_data(impath, 'out', text)
#     return text
# # if __name__ == '__main__':
# #     # dir = "runs\detect\exp"
# #     # path = os.path.join(dir, '1.jpg')
# #     number = read_string()
# #     print(number)
#
# if __name__ == '__main__':
#     path_ocr = './runs/detect/exp/bsxot.jpg'
#     path_yolo = 'D:/Yolov7_OCR/yolov7/inference/vid.mp4'
#     d = threading.Thread(name='ocr', target=ocr,args=(path_ocr,))
#     d.setDaemon(True)
#     t = threading.Thread(name='yolo', target=detect_export, args=(path_yolo,))

    # d.start()
    # t.start()

import easyocr
import cv2
from matplotlib import pyplot as plt
import os
import numpy as np

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
        img = cv2.putText(img, text, (20, spacer), font, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
        spacer += 15


    #plt.imshow(img)

    #plt.show()
    return text
if __name__ == "__main__":
    root = 'D:/Yolov7_OCR/yolov7/runs/detect/exp4/crops/licence-plate'
    path = os.path.join(root, 'test.jpg')
    ocr(path)