from PIL import Image
import pytesseract

path = '/Users/malamapono/Desktop/lat.png'
image = Image.open(path)
text = pytesseract.image_to_string(image)
print(text)