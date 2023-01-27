# import the necessary packages
# from PIL import Image
import pytesseract
from glob import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
img_paths = glob('*.jpg')
results=[]
for i in img_paths:
    results.append(pytesseract.image_to_string(i, lang='eng'))

for i in results:
    print(i, end='\n----------------------------------------\n')