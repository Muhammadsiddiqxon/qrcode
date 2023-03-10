import cv2module
from pyzbar import pyzbar

img = cv2module.imread('ัะตัั.png')
barcodes = pyzbar.decode(img)

for barcode in barcodes:
    barcodeData = barcode.data.decode('utf-8')
    print(f'Result: {barcodeData}')