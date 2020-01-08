from wordcloud import WordCloud, STOPWORDS
import string
import re
import numpy as npy
from PIL import Image

processedTxtPath = "assets/gay-seattle-processed.txt"
wcPath = "img/gay-seattle.png"

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

stopwords = set(STOPWORDS)
removewords = {"time", "one", "began", "among", "another", "see", "part", "many", "day", "day", "way", "times",
               "still", "news", "three", "came", "became", "made", "wanted", "seemed", "made", "now", "society",
               "ing", "time", "first", "new", "called", "said", "come", "two", "city", "group", "state", "year",
               "case", "member", "even", "later", "month", "years", "much", "week", "county", "name", "example"
               "well", "members", "us", "say"}
stopwords.update(removewords)


print(txt)
print("generating wordcloud...")
mask_array = npy.array(Image.open("img/cloud.jpg"))
wc = WordCloud(font_path='arial', background_color="white", max_words=50, prefer_horizontal=1, mask=mask_array, scale=3, stopwords=stopwords, collocations=False)
# wc.generate_from_frequencies(txt)
wc.generate(txt)
wc.to_file(wcPath)
print("completed!")
