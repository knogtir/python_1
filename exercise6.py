from collections import Iterable
def findMinAndMax(l):
    if isinstance(l, Iterable):
        min = l[0]
        max = l[0]
        for x in l:
            if x < min:
                min = x
        for x in l:
            if x > max:
                max = x
        return (min, max)
    else:
        return (None, None)
            
