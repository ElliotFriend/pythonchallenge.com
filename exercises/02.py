# This URL: http://www.pythonchallenge.com/pc/def/ocr.html
# Next URL: 
import string
# view the page source to get to the real part of the riddle
f = open('/home/elliot/Development/pythonchallenge.com/data/02.txt', 'r')
alphanumeric = string.ascii_lowercase + str('0123456789')
letters_and_numbers = []
print alphanumeric
for line in f:
    for letter in line:
        if letter in alphanumeric:
            letters_and_numbers.append(letter)
            
print letters_and_numbers
