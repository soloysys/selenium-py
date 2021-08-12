import pytesseract
from PIL import Image
image = Image.open('E:/code1.png')

text = pytesseract.image_to_string(image)
print(text)
