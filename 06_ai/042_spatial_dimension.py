import spacy
import pickle

# read text file
print("reading text file...")
with open("C:\\Users\\Jou Ho\\Desktop\\no_blank_native_seattle.txt") as txt_file:
    text = txt_file.read()

#  "nlp" Object is used to create documents with linguistic annotations.
nlp = spacy.load("en_core_web_sm")
my_doc = nlp(text)

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

# remove duplicates from the list
# print("removing duplicates...")
# print("number of items in the old list:" + str(len(lemma_sent)))
# rem_dup = list(dict.fromkeys(lemma_sent))
# print("number of items in the new list:" + str(len(rem_dup)))
# print(rem_dup)

# remove blanks (\n\n)
nb_data = []
for word in lemma_sent:
    if word != '\n\n':
        nb_data.append(word)
print("no blank data: ", nb_data)

# make all the words into lowercase
clean_data = [x.lower() for x in nb_data]
print("clean data: ", clean_data)

# convert python objects into string representation for later use
print("pickling the list...")
with open("C:\\Users\\Jou Ho\\Desktop\\NS_pickled.txt", "wb") as fp:
    pickle.dump(clean_data, fp)
