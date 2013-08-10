# This URL: http://www.pythonchallenge.com/pc/def/ocr.html
# Next URL: http://www.pythonchallenge.com/pc/def/equality.html
import string
# view the page source to get to the real part of the riddle
text = open('/home/elliot/GitHub/pythonchallenge.com/data/02.txt', 'r').read()

print filter(lambda x: x in string.letters, text)
