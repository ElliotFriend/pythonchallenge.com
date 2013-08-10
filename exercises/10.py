# This URL: http://www.pythonchallenge.com/pc/return/bull.html
# Next URL: http://www.pythonchallenge.com/pc/return/5808.html

import itertools

#a = [1, 11, 21, 1211, 111221]

def A005150(n):
    p = "1"
    seq = [1]
    while (n > 1):
        q = ''
        idx = 0 # Index
        l = len(p) # Length
        while idx < l:
            start = idx
            idx = idx + 1
            while idx < l and p[idx] == p[start]:
                idx = idx + 1
            q = q + str(idx-start) + p[start]
        n, p = n - 1, q
        seq.append(int(p))
    return seq

a = A005150(35)
print len(str(a[30]))
