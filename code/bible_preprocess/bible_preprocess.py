import os
import re

import nltk
from nltk.tokenize import sent_tokenize


IN_FILE = "/veld/input/" + os.getenv("in_file")
OUT_FILE = "/veld/output/" + os.getenv("out_file")


# load sentence splitting function
nltk.download('punkt')


with open(IN_FILE, "r") as f:
    content = f.read()

content = content.lower()
content = content.replace("\r\n", " ")
content = content.replace("\n", " ")
content = re.sub("\d+:\d+ ", "", content)
content = sent_tokenize(content)

# write to file, one sentence per line
with open(OUT_FILE, "w") as f:
    for line_nr, sentence in enumerate(content):
        # from line 29792 onwards, there is only gutenberg metadata left, so break the loop
        if line_nr == 29792:
            break
        f.write(sentence + "\n")

