import string

# This URL: http://www.pythonchallenge.com/pc/def/map.html
# Next URL: http://www.pythonchallenge.com/pc/def/ocr.html
#
# We need to map one sentence a couple letters over. Here's our clue:
# K -> M
# O -> Q
# E -> G
# "everybody thinks twice before solving this."
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
#     | |   | | | |
#     ---   --- ---
# Here's the text to transcode:
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq
qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

alphabet = string.ascii_lowercase[:26]
code = string.ascii_lowercase[2:] + string.ascii_lowercase[:2]
trans = string.maketrans(alphabet, code)
url = "map"


print text.translate(trans)
print url.translate(trans)
