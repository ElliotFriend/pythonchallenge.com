# This URL: http://www.pythonchallenge.com/pc/return/italy.html
# Next URL: http://www.pythonchallenge.com/pc/return/uzi.html

import Image

imageA = Image.open('../data/wire.png', 'r')
imageB = Image.new('RGB', (100,100), (0,0,0))

def get_image_line(source, destination, start, end, location, across, increment, position):
    for n in range(start, end, increment):
        if across:
            destination.putpixel((n, location), source.getpixel((position, 0)))
        else:
            destination.putpixel((location, n), source.getpixel((position, 0)))
        position += 1
    
    if across:
        location += increment
    else:
        location -= increment
    
    return position, location

i, xmin, ymin, xmax, ymax = 0, 0, 0, 99, 99

while( xmax >= 0 and ymax >= 0 ):
    i, ymin = get_image_line(imageA, imageB, xmin, xmax+1, ymin, True, 1, i)
    i, xmax = get_image_line(imageA, imageB, ymin, ymax+1, xmax, False, 1, i)
    i, ymax = get_image_line(imageA, imageB, xmax, xmin-1, ymax, True, -1, i)
    i, xmin = get_image_line(imageA, imageB, ymax, ymin-1, xmin, False, -1, i)
    
imageB.save('../data/spiral.png')
