"""
A simple script for transforming the green
pixels in an image into alpha pixels (transparent).
The gray scale channel is transformed into
alpha channel.
"""

from PIL import Image
image = Image.open("input.png").convert('RGBA')
pixeldata = list(image.getdata())

for i,pixel in enumerate(pixeldata):
    if pixel[:3] == (0,255,0):
        pixeldata[i] = (255,255,255,0)

image.putdata(pixeldata)
image.save("output.png")