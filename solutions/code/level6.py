#!/usr/bin/env python
from PIL import Image

IMAGE_SIZE = 255
INPUT_FILENAME = 'input.png'
RESULT_FILENAME = 'result.png'

# Generates the QR Code from alpha values in input.png.
if __name__ == '__main__':
    input_image = Image.open(INPUT_FILENAME)
    result_image = Image.new('1', (IMAGE_SIZE, IMAGE_SIZE), 'white')
    pixels = result_image.load()
    for i in range(IMAGE_SIZE):
        for j in range(IMAGE_SIZE):
            (_,_,_,a) = input_image.getpixel((i,j))
            if a == 255:
                pixels[i,j] = 0;
    result_image.save(RESULT_FILENAME)
