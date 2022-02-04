import spacy
import re
import string
import nltk
from nltk.probability import FreqDist
import pickle

# read text file
print("reading text file...")
processedTxtPath = "assets/gay-seattle-processed.txt"
with open(processedTxtPath, "r", encoding="utf8") as txt_file:
    txt = txt_file.read()

# Convert text to lowercase
txt = txt.lower()
# Remove numbers
txt = re.sub(r'\d+', '', txt)

# Remove punctuation
txt = re.sub(r'[^\w\s]', '', txt)

# delete the white spaces
# https://www.journaldev.com/23763/python-remove-spaces-from-string#python-remove-whitespaces-from-string-using-regex
txt = " ".join(txt.split())
txt.translate({ord(c): None for c in string.whitespace})

txt = txt.replace("gays", "gay").replace("lesbians", "lesbian").replace("seattles", "seattle").replace("citys", "city")
print(txt)

#  "nlp" Object is used to create documents with linguistic annotations.
nlp = spacy.load("en_core_web_sm")
nlp.max_length = len(txt)
my_doc = nlp(txt)

# tokenizing the text
print("tokenizing the text...")
token_list = []
for token in my_doc:
    token_list.append(token)
print("list of tokens:", token_list)

# removing stopwords
print("removing stop words...")
filtered_sent = []
for word in my_doc:
    if not word.is_stop:
        filtered_sent.append(word)
print("Filtered words: ", filtered_sent)

# lemmatization
print("lemmatizing...")
lemma_sent = []
for word in filtered_sent:
    lemma_sent.append(word.lemma_)
print("lemmatized data: ", lemma_sent)
processedTxt = " ".join(lemma_sent)
processedDoc = nlp(processedTxt)

geoTxt = ""
for ent in processedDoc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)
    if ent.label_ == "GPE":
        geoTxt += ent.text.replace(" ", "") + " "


# tokenize and calculate the word frequencies
tokens = nltk.tokenize.word_tokenize(geoTxt)
fDist = FreqDist(tokens)
with open("assets/gay-seattle-places.csv", "w", encoding="utf8") as fp:
    for item in fDist.most_common(300):
        try:
            fp.write("%s, %d\n" % (item[0].replace("county", " county").replace("state", " state").replace("city", " city"), item[1]))
            print(item)
        except TypeError as error:
            pass
print("finished!")






