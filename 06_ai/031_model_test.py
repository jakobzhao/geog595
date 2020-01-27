from gensim.models import Word2Vec

# test model
print('loading model...')
model = Word2Vec.load("assets/gay-seattle.w2v")
print("seattle", model.wv.most_similar('seattle', topn=50))

print(model.wv.distances('seattle', ('news', 'june', 'times', 'march')))

# seattle [('news', 0.9989323616027832), ('june', 0.998815655708313), ('times', 0.9987982511520386), ('march', 0.9987823963165283), ('apr', 0.9987049102783203), ('july', 0.9985809326171875), ('nov', 0.9984444379806519),


# print("model details: ", model)
# print('similar words to seattle:')
# print("capitol", model.wv.most_similar('capitol'))
#
# print("gay", model.wv.most_similar('gay', topn=50))
# print(model.wv.most_similar('lesbian'))
# print(model.wv.most_similar('considered'))
# print(model.wv.most_similar('number'))
# print("=================")
# print(model.wv.distances('seattle', ('gay', 'renton', 'lesbian', 'rain')))
# print(model.wv.distance('seattle', 'civil'))
# print(model.wv.distance('seattle', 'lesbian'))
# print(model.wv.rank('seattle', 'gay'))
# print(model.wv.rank('seattle', 'lesbian'))
# print(model.wv.distances('seattle'))
