from PIL import Image, ImageDraw
import os

pasta = 'semmarca'

for imagen in os.listdir(pasta):
    imagename = imagen
    img = Image.open('semmarca/' + imagename)
    drawing = ImageDraw.Draw(img)
    drawing.text((50, 50), "VICTORH8")
    img.save(f'commarca/{imagen}')
        
