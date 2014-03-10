# This URL: http://www.pythonchallenge.com/pc/def/equality.html
# Next URL: http://www.pythonchallenge.com/pc/def/linkedlist.html

import re

answer = ""

text = open("../data/03.txt", "r")
for i in re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text.read()):
    answer += i[len(i) // 2]

print answer
text.close()
