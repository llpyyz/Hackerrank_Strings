"""
David Schonberger
Hackerrank.com
Strings - pangram check
1/23/2015
"""
s = raw_input()
s = s.split(' ')
l = []
s = [elt.lower() for elt in s]
for elt in s:
    res = [ch for ch in elt]
    l += res
l = list(set(l))
if(len(l) == 26):
    print 'pangram'
else:
    print 'not pangram'
