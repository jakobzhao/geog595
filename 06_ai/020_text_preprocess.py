import re
import string
from nltk.corpus import stopwords
import nltk.data
import pickle
# https://medium.com/@datamonsters/text-preprocessing-in-python-steps-tools-and-examples-bf025f872908
txtPath = "assets/gay-seattle.txt"
processedTxtPath = "assets/gay-seattle-processed.txt"

# read text file
print("reading text file...")
txt = ""
with open(txtPath, "r", encoding="utf8") as txt_file:
    txt = txt_file.read()

# Convert text to lowercase
txt = txt.lower()
# Remove numbers
# txt = re.sub(r'\d+', '', txt)

# Remove punctuation
# txt = re.sub(r'[^\w\s]', '', txt)

# delete the white spaces
# https://www.journaldev.com/23763/python-remove-spaces-from-string#python-remove-whitespaces-from-string-using-regex
txt = " ".join(txt.split())
# txt.translate({ord(c): None for c in string.whitespace})

with open(processedTxtPath, "w", encoding="utf8") as output:
    output.write(txt)

print(txt)
print("finished!")