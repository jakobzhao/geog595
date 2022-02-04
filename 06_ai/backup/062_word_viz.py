from sklearn.decomposition import IncrementalPCA    # inital reduction
from sklearn.manifold import TSNE                   # final reduction
import numpy as np                                  # array handling
from gensim.models import Word2Vec

from wordcloud import STOPWORDS
import nltk
from nltk.probability import FreqDist
import string
import re

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


tokens = nltk.tokenize.word_tokenize(txt)
fDist = FreqDist(tokens)

model = Word2Vec.load("assets/gay-seattle.w2v")


def reduce_dimensions(model):
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    vectors = [] # positions in vector space
    labels = [] # keep track of words to label our data again later
    for word in model.wv.vocab:
        vectors.append(model.wv[word])
        labels.append(word)

    # convert both lists into numpy vectors for reduction
    vectors = np.asarray(vectors)
    labels = np.asarray(labels)

    # reduce using t-SNE
    vectors = np.asarray(vectors)
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    return x_vals, y_vals, labels


x_vals, y_vals, labels = reduce_dimensions(model)
with open("assets/gay-seattle-pnts.csv", "w+", encoding="utf8") as fp:
    i = 0
    fp.write("id, x, y, freq, label\n")
    for label in labels:
        fp.write("%d, %f, %f, %d, %s\n" % (i, x_vals[i], y_vals[i], fDist[label], label))
        i += 1

print("finished!")

