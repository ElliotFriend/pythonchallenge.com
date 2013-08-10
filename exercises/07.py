# This URL: http://www.pythonchallenge.com/pc/def/oxygen.html
# Next URL: http://www.pythonchallenge.com/pc/def/integrity.html

import re, Image

im = Image.open('/home/elliot/GitHub/pythonchallenge.com/data/07.png')
row = [im.getpixel((x, 45)) for x in range(0, im.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))
