# This URL: http://www.pythonchallenge.com/pc/def/peak.html
# Next URL: http://www.pythonchallenge.com/pc/def/channel.html

import urllib,pickle

url = "http://www.pythonchallenge.com/pc/def/banner.p"
obj = pickle.load(urllib.urlopen(url))

for i in obj:
    print ''.join(map(lambda pair: pair[0]*pair[1], i))
