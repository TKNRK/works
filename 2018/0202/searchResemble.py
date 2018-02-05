from gensim import models

DOC_PATH = './lines/{0}.txt'

model = models.Doc2Vec.load('d2v-full.model')
# model = models.Doc2Vec.load('d2v.model')

# 似た文章を探す
def search_similar_texts(path):
    most_similar_texts = model.docvecs.most_similar(path)
    for similar_text in most_similar_texts:
        print(similar_text)
        with open(similar_text[0], "r") as r:
            for row in r:
                print(row)


if __name__ == '__main__':
    print('ID:')
    ID = input()
    print()
    if len(ID) == 1:
        ID = "0" + ID
    document = DOC_PATH.format(ID)

    with open(document, "r") as r:
        for row in r:
            print(row)

    search_similar_texts(document)