import re
from nltk.corpus import stopwords
import nltk.data
import pickle
from multiprocessing import cpu_count
from gensim.models import Word2Vec

processedTxtPath = "assets/gay-seattle-processed.txt"
pickledTxtPath = "assets/gay-seattle-pickled.bin"
modelPath = "assets/gay-seattle.w2v"


def review_to_wordlist(review, remove_stopwords=False):
    # Function to convert a document to a sequence of words,
    # optionally removing stop words.  Returns a list of words.
    #
    # 1. Remove HTML
    # review_text = BeautifulSoup(review, 'html5lib').get_text()
    #
    # 2. Remove non-letters
    review_text = re.sub("[^a-zA-Z]", " ", review)
    #
    # 3. Convert words to lower case and split them
    words = review_text.lower().split()
    #
    # 4. Optionally remove stop words (false by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    #
    # 5. Return a list of words
    return words


# Define a function to split a review into parsed sentences
def review_to_sentences(review, tokenizer, remove_stopwords=False):
    # Function to split a review into parsed sentences. Returns a
    # list of sentences, where each sentence is a list of words
    #
    # 1. Use the NLTK tokenizer to split the paragraph into sentences
    raw_sentences = tokenizer.tokenize(review.strip())
    #
    # 2. Loop over each sentence
    sentences = []
    for raw_sentence in raw_sentences:
        # If a sentence is empty, skip it
        if len(raw_sentence) > 0:
            # Otherwise, call review_to_wordlist to get a list of words
            new_sentence = review_to_wordlist(raw_sentence, remove_stopwords)
            if new_sentence != [] and new_sentence != [u'none']:
                sentences.append(new_sentence)
    # Return the list of sentences (each sentence is a list of words,
    # so this returns a list of lists
    return sentences


if __name__ == "__main__":
    # download the punkt tokenizer for sentence splitting
    # nltk.download()
    # load the tokenizer
    print('loading the tokenizer...')
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    # read text file
    print("reading text file...")
    with open(processedTxtPath, "r", encoding="utf8") as txt_file:
        text = txt_file.read()

    pickedTxt = review_to_sentences(text, tokenizer, remove_stopwords=True)
    data = [d for d in pickedTxt]
    # convert python objects into string representation for later use
    print("pickling the list...")
    with open(pickledTxtPath, "wb+") as fp:
        pickle.dump(data, fp)

    with open(pickledTxtPath, "rb") as fp:
        doc = pickle.load(fp)

    # train a model
    print("creating a model...")
    model = Word2Vec(doc, workers=cpu_count())
    model.save(modelPath)
    print("completed!")
