from os import listdir
from os.path import isfile, join
unparsed_textfiles = [f for f in listdir("../Unparsed/") if isfile(join("../Unparsed/", f))]
parsed_textfile = [f for f in listdir("../Texts") if isfile(join("../Texts", f))]
for fname in unparsed_textfiles:
    if fname in parsed_textfile:
        continue
    f = open(join("../Unparsed/", fname), mode="r")

