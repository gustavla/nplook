
from __future__ import print_function
import sys
import numpy as np

def represent(obj):
    if isinstance(obj, np.ndarray):
        return "ndarray: {0} [{1}]".format(obj.shape, obj.dtype)
    else:
        return repr(obj)

def summarize(filename):
    s = ""
    try:
        data = np.load(filename)
    except IOError:
        data = None

    status = ''
    if data is None:
        status = 'FILE NOT FOUND!'

    s += "-> {0} {1}\n".format(filename, status)
    
    if data:
        N = max(map(lambda x: len(x), data.keys()))
        indent = 3
        for k in data.keys():
            x = represent(data[k])
            x = x.replace('\n', '\n'+' '*(N+2 + indent))
            s += " "*indent + "{0} : {1}\n".format(k.rjust(N), x)
    # Remove the last newline
    if s[-1] == '\n':
        s = s[:-1]
    return s


if __name__ == '__main__':
    filenames = sys.argv[1:]
    if filenames:
        for i, fn in enumerate(filenames):
            if i != 0: print()
            print(summarize(fn))
    else:
        print("Usage: npzlook file1 [file2, ...]")
        print(" ex. npzlook data*.npz")
