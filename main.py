from numpy import double
from pytesseract import*
import numpy as np
import cv2


pytesseract.tesseract_cmd = r'C:\\Users\\ambro\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

min_conf = 40

image = cv2.imread("img.png")



image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(image, output_type=Output.DICT)

for i in range(0, len(results["text"])):
    
    # We can then extract the bounding box coordinates
    # of the text region from the current result
    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    
    # We will also extract the OCR text itself along
    # with the confidence of the text localization
    text = results["text"][i]
    conf = float(results["conf"][i])
    
    # filter out weak confidence text localizations
    if conf > min_conf:
        print(text, end=" ")


