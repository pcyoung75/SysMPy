import spacy
import re
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn import metrics
import spacy
import re
import pandas as pd
from sklearn.svm import LinearSVC
from sklearn import metrics
from spacy.tokens import Token

# who, what, when, where, why, and how
# wo, wa, wn, wr, wy, hw
# Who   what2(to what)	why     when    where   what    How     How Much    Verb    Aux. V
# wo    tw              wy      wn      wr      wh      hw      hm          vb      av


class spacy_doc():
    def __init__(self, txt):
        nlp = spacy.load("en_core_web_sm")
        self.doc = nlp(txt)

    def print(self, width=6):
        tokens = []
        print_temp = ''
        for i, token in enumerate(self.doc):
            t = [token.text, token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop]
            tokens.append(t)

        for i in range(len(tokens[0])):
            print_temp += '{v'+str(i)+':'+'{w0}} '

        el = ['text', 'lemma', 'pos', 'tag', 'dep', 'shape', 'alpha', 'stop']
        print(print_temp.format(v0=el[0],v1=el[1], v2=el[2], v3=el[3], v4=el[4], v5=el[5], v6=el[6], v7=el[7], w0=width))

        for el in tokens:
            print(print_temp.format(v0=el[0],v1=el[1], v2=el[2], v3=el[3], v4=el[4], v5=el[5], v6=el[6], v7=el[7], w0=width))

    def print_chunk(self):
        for chunk in self.doc.noun_chunks:
            print(chunk.text, chunk.root.text, chunk.root.dep_, chunk.root.head.text)

class Extractor5W1H(spacy_doc):
    def __init__(self, txt):
        super().__init__(txt)
        self.info = {}

    def extract(self, token):
        lemma, pos, tag, dep = token.lemma_, token.pos_, token.tag_, token.dep_
        if pos == 'NOUN' and tag == 'NNS' and dep == 'nsubj':
            self.info['WHO'] = token
        elif pos == 'VERB' and tag == 'VBP' and dep == 'ROOT':
            self.info['VERB'] = token
        elif pos == 'NOUN' and tag == 'NN' and dep == 'dobj':
            self.info['WHAT'] = token
        elif pos == 'NOUN' and tag == 'NNS' and dep == 'pobj':
            self.info['TOWHAT'] = token

    def token_to_chunk(self, chunk):
        for k, v in self.info.items():
            # print(id(chunk.root), id(v))
            if isinstance(v, Token):
                if chunk.root == v:
                    self.info[k] = chunk

    def run(self, width=6):
        # Extract basic information about 5W1H
        for i, token in enumerate(self.doc):
            self.extract(token)

        # Convert a token to a noun chunk
        for chunk in self.doc.noun_chunks:
            self.token_to_chunk(chunk)

        return self.info


txt = "Autonomous cars shift insurance liability toward manufacturers"
# txt = 'I do not know with whom I will go to the prom.'
sp = Extractor5W1H(txt)

print(sp.run())