# 参考：https://github.com/Foo-x/doc2vec-sample/blob/master/doc2vec.py

import os
import sys
import collections
import polyglot
from polyglot.text import Text, Word
from gensim import models
from gensim.models.doc2vec import LabeledSentence


INPUT_DOC_DIR = "./lines/"
OUTPUT_MODEL = "d2v.model"
PASSING_PRECISION = 93
NUM = 69

def get_all_files(directory):
    lst = []
    for i in range(NUM):
        if i<10:
          s = "0" + str(i)
        else:
          s = str(i)
        lst.append("./lines/" + s + ".txt")
    return lst



# 改行コードを抜き忘れたので，ここで抜く
def read_document(path):
    with open(path, 'r', errors='ignore') as f:
        return Text(f.read()[:-1])


def split_into_words(doc, name=''):
    tags = doc.pos_tags
    words = []
    for tag in tags:
      if tag[1] != "PUNCT":
        words.append(str(tag[0]))
    return LabeledSentence(words=words, tags=[name])


def corpus_to_sentences(corpus):
    docs = [read_document(x) for x in corpus]
    for idx, (doc, name) in enumerate(zip(docs, corpus)):
        sys.stdout.write('\r前処理中 {} / {}'.format(idx, len(corpus)))
        yield split_into_words(doc, name)


def train(sentences):
    model = models.Doc2Vec(size=400, alpha=0.0015, sample=1e-4, min_count=1, workers=4)
    model.build_vocab(sentences)
    for x in range(10):
        print(x)
        model.train(sentences, total_examples=model.corpus_count, epochs=model.iter)
        ranks = []
        for doc_id in range(NUM):
            inferred_vector = model.infer_vector(sentences[doc_id].words)
            sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
            rank = [docid for docid, sim in sims].index(sentences[doc_id].tags[0])
            ranks.append(rank)
        print(collections.Counter(ranks))
        if collections.Counter(ranks)[0] >= PASSING_PRECISION:
            break
    return model


if __name__ == '__main__':
    corpus = get_all_files(INPUT_DOC_DIR)
    sentences = list(corpus_to_sentences(corpus))
    print()
    model = train(sentences)
    model.save(OUTPUT_MODEL)

