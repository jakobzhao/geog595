from gensim.models import Word2Vec
import networkx as nx
from wordcloud import STOPWORDS
import nltk
from nltk.probability import FreqDist
import string
import re
import numpy as npy
from PIL import Image

processedTxtPath = "assets/gay-seattle-processed.txt"


# load the dataset
print("loading text data...")
txt = open(processedTxtPath, "r", encoding="utf8").read()

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
# print(txt)

stopwords = set(STOPWORDS)
commonwords = {"time", "one", "began", "among", "another", "see", "part", "many", "day", "day", "way", "times",
               "still", "news", "three", "came", "became", "made", "wanted", "seemed", "made", "now", "society",
               "ing", "time", "first", "new", "called", "said", "come", "two", "city", "group", "state", "year",
               "case", "member", "even", "later", "month", "years", "much", "week", "county", "name", "example"
               "well", "members", "us", "say", "s"}
stopwords.update(commonwords)

# tokenize and calculate the word frequencies
tokens = nltk.tokenize.word_tokenize(txt)
fDist = FreqDist(tokens)
# print(fDist.most_common(20))

# remove the stop words and common words
filtered_fDist = nltk.FreqDist(dict((word, freq) for word, freq in fDist.items() if word not in stopwords))

words = []
for item in filtered_fDist.most_common(50):
    words.append(item[0])

print(words)
print('loading model...')
model = Word2Vec.load("assets/gay-seattle.w2v")
g = nx.DiGraph()
g.add_nodes_from(words)
allwords = words
for mainWord in allwords:
    words.remove(mainWord)
    for word in words:
        try:
            score = model.wv.distance(mainWord, word)
            if score < 0.02:
                print("%s --> %s: %8.5f" % (mainWord, word, score))
                g.add_edge(mainWord, word, weight=int(score * score * 1000000))
        except:
            pass
    # words.append(mainWord) # perhaps not necessary



nx.write_gexf(g, "assets/gay-seattle.gexf", encoding='utf-8', prettyprint=True, version='1.1draft')
print("finished!")
