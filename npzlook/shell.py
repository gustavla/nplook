
from __future__ import print_function
import sys
import npzlook
from optparse import OptionParser

def main():
    examples = []
    examples.append(("data.npz", "inspects the file data.npz"))
    examples.append(("*.npz", "summarizes all npz files in the directory"))

    ex_str = "\n".join(["  %prog {0:<18}{1}".format(tup[0], tup[1]) for tup in examples])

    usage = "Usage: %prog [options] <file> [<file> ...]\n\nExamples:\n{0}".format(ex_str)
    parser = OptionParser(usage=usage, version="%prog {0}".format(npzlook.__version__))

    (options, args) = parser.parse_args()
    
    for filename in args:
        for i, fn in enumerate(filenames):
            if i != 0: print()
            print(npzlook.summarize(fn))
