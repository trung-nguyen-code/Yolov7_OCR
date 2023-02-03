import cv2
import easyocr
import os
import numpy as np
import imutils


def ocr(img):
    # root = './'
    # path = os.path.join(root, path)
    # image = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # threshold the image using Otsu's thresholding method
    thresh = cv2.threshold(gray, 0, 255,
                           cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]

    # apply a distance transform which calculates the distance to the
    # closest zero pixel for each pixel in the input image
    dist = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    # normalize the distance transform such that the distances lie in
    # the range [0, 1] and then convert the distance transform back to
    # an unsigned 8-bit integer in the range [0, 255]
    dist = cv2.normalize(dist, dist, 0, 1.0, cv2.NORM_MINMAX)
    dist = (dist * 255).astype("uint8")
    # threshold the distance transform using Otsu's method
    dist = cv2.threshold(dist, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # apply an "opening" morphological operation to disconnect components
    # in the image
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    opening = cv2.morphologyEx(dist, cv2.MORPH_OPEN, kernel)

    # find contours in the opening image, then initialize the list of
    # contours which belong to actual characters that we will be OCR'ing
    cnts = cv2.findContours(opening.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    chars = []
    # loop over the contours
    for c in cnts:
        # compute the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(c)
        # check if contour is at least 35px wide and 100px tall, and if
        # so, consider the contour a digit
        if w >= 1 and h >= 10:
            chars.append(c)

    # compute the convex hull of the characters
    chars = np.vstack([chars[i] for i in range(0, len(chars))])
    hull = cv2.convexHull(chars)
    # allocate memory for the convex hull mask, draw the convex hull on
    # the image, and then enlarge it via a dilation
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.drawContours(mask, [hull], -1, 255, -1)
    mask = cv2.dilate(mask, None, iterations=2)
    # take the bitwise of the opening image and the mask to reveal *just*
    # the characters in the image
    final = cv2.bitwise_and(opening, opening, mask=mask)

    # cv2.imshow("final", final)
    # cv2.waitKey()

    reader = easyocr.Reader(['en'])
    text = None
    result = reader.readtext(final)
    for detection in result:
        text = detection[1]
    return text


# if __name__ == '__main__':
#     root = './'
#     path = os.path.join(root, 'runs/detect/exp12/crops/licence-plate/0.jpg')
#     print(ocr(path))
