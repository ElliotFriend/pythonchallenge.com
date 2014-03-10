# This URL: http://www.pythonchallenge.com/pc/return/evil.html
# Next URL: http://www.pythonchallenge.com/pc/return/disproportional.html

evil = open('../data/evil2.gfx', 'r').read()
image1 = open('../data/image1.jpg', 'w')
image2 = open('../data/image2.jpg', 'w')
image3 = open('../data/image3.jpg', 'w')
image4 = open('../data/image4.jpg', 'w')
image5 = open('../data/image5.jpg', 'w')

for i in range(0, len(evil), 5):
    image1.write(evil[i])
    image2.write(evil[i+1])
    image3.write(evil[i+2])
    image4.write(evil[i+3])
    image5.write(evil[i+4])

image1.close()
image2.close()
image3.close()
image4.close()
image5.close()
