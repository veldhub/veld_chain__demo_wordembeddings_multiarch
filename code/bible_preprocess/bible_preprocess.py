import os
import re

import nltk
import string


print("-- bible preprocessing: start -------------------------------------------")
IN_FILE = "/veld/input/" + os.getenv("in_file")
OUT_FILE = "/veld/output/" + os.getenv("out_file")
print("IN_FILE:", IN_FILE)
print("OUT_FILE:", OUT_FILE)


# load sentence splitting function
nltk.download('punkt')

# read file
with open(IN_FILE, "r") as f:
    content = f.read()

# transform content
content = content.lower()
content = content.replace("\r\n", " ")
content = content.replace("\n", " ")
content = re.sub("\d+:\d+ ", "", content)
sentence_list = []
for sentence in nltk.sent_tokenize(content):
    word_list_new = []
    for word in nltk.word_tokenize(sentence):
        if word not in string.punctuation:
            word_list_new.append(word)
    sentence_list.append(" ".join(word_list_new))

# from line 29792 onwards, there is only gutenberg metadata left. So cut that
sentence_list = sentence_list[:29792]

# write to file, one sentence per line
with open(OUT_FILE, "w") as f:
    for sentence in sentence_list:
        f.write(sentence + "\n")

print("-- bible preprocessing: done --------------------------------------------")

