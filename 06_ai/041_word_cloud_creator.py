from wordcloud import WordCloud, STOPWORDS
import numpy as npy
from PIL import Image

# load the dataset
print("loading text data...")
data_set = open("C:\\Users\\Jou Ho\\Desktop\\no_blank_gay_seattle.txt").read()


# define a function to generate wordcloud
def create_wordcloud(string):
    mask_array = npy.array(Image.open("C:\\Users\\Jou Ho\\Desktop\\WA.png"))
    cloud = WordCloud(background_color="white", max_words=200, mask=mask_array, stopwords=set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("gay_seattle_WC.png")


# change all the characters to lowercase
data_set = data_set.lower()
# generate word cloud and save the image as png file
print("generating wordcloud...")
create_wordcloud(data_set)
print("completed!")
