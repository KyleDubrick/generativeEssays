from os import listdir
from os.path import isfile, join, isdir
import re
import sys
# Search recursively for files. Returns array of filenames or empty array
def search_rfile(path):
    result = []
    for fna in listdir(path):
        fna = join(path, fna)
        if isdir(fna):
            result.extend(search_rfile(fna))
        elif isfile(fna):
            result.append(fna)
    return result

def parse(txt):
    txt = txt.lower()
    txt = re.sub("[^a-z,']", " ", txt)
    txt = re.sub("\d", " ", txt)
    txt = re.sub("\s{2,}", " ", txt)
    txt = txt.strip()
    return txt

test1 = ["Hi this is a test #1! How's it going?", "hi this is a test how's it going"]
test2 = ["and then he said:\"Wow! This is test #2.\"", "and the he said wow this is test"]
test3 = ["Here\n Comes\n THAT\n BOIII\n 12345", "here comes that boiii"]
test4 = [" My moMMa told me to forget11 about thiss1", "my momma told me to forget about thiss"]
print(parse(test1[0]) + "\n" + test1[1] + "\n\"" + test1[1][len(test1[1]) - 1] + "\"")

# unparsed_textfiles = search_rfile("../Unparsed")
# parsed_textfile = search_rfile("../Texts")
# for fname in unparsed_textfiles:
#     if fname in parsed_textfile:
#         continue
#     txt = open(fname, mode="r").read()
#     txt = re.sub("\s{2,}"," ",re.sub("\W", " ",txt.lower()))
#     open(fname.replace("Unparsed","Texts"), mode="w+").write(txt)