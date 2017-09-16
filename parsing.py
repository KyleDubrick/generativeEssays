from os import listdir
from os.path import isfile, join
textfiles = [f for f in listdir("../Unparsed") if isfile(join("../Unparsed", f))]

for fname in textfiles:
    f = open(fname, mode="r")
    