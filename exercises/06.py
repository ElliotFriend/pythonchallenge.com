# This URL: http://www.pythonchallenge.com/pc/def/channel.html
# Next URL: http://www.pythonchallenge.com/pc/def/oxygen.html


import zipfile

zfile = zipfile.ZipFile(open('/home/elliot/GitHub/pythonchallenge.com/data/06.zip', 'r'))
next_nothing = "Next nothing is "
nothing = "90052"
suffix = ".txt"
answer = []

for name in zfile.namelist():
    data = zfile.read(nothing + suffix)
    if next_nothing in data:
        current_nothing = nothing + suffix
        print data
        comment = zfile.getinfo(current_nothing).comment
        answer.append(comment)
        _,nothing = data.split(next_nothing)
    else:
        zfile.close()
        print "Answer :: "
        print "".join(answer)
        exit(0)
