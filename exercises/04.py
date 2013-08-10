# This URL: http://www.pythonchallenge.com/pc/def/linkedlist.php
# Next URL: http://www.pythonchallenge.com/pc/def/peak.html

import urllib

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"
first_nothing = "12345"
nothing = first_nothing
nothing_text = 'and the next nothing is '

for i in range(0, 400):
    page = urllib.urlopen(url % nothing).read()
    if nothing_text in page:
        _,nothing = page.split(nothing_text)
        print page
    elif "Divide by two" in page:
        nothing = int(nothing) / 2
        print page
    else:
        print "end of nothings?"
        print page
        exit(0)
