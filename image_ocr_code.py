# import the necessary packages
# from PIL import Image
import pytesseract
from glob import glob

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def main():
    img_paths = glob('*.jpg')
    # results=[]
    for i in img_paths:
        print(pytesseract.image_to_string(i, lang='eng'), end='\n------------------------\n')
        
if __name__=='__main__':
    main()