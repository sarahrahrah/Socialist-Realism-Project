import numpy as np
import pandas as pd
from nltk.corpus import stopwords 
import string
import gensim
from gensim import corpora
from gensim import models
import matplotlib.pyplot as plt
import plotly
print(plotly.__version__)  # version >1.9.4 required
from plotly.graph_objs import Scatter, Layout
import collections
from collections import OrderedDict


ourdata = pd.read_csv("LITERATURE.csv")

thetext = ourdata["text"]

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("russian")

stop = set(stopwords.words('russian'))


otherstopwords = ["это","да","наш","сво","одн","говор","сказа","нам","—","котор","мо","очен"]
otherstop = set(otherstopwords)

stop.update(otherstop)



exclude = set(string.punctuation) 

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
    stop_freeagain = " ".join([i for i in punc_free.split() if i not in stop])
    joined = " ".join([stemmer.stem(word) for word in stop_freeagain.split()])
    stopfree2 = " ".join([i for i in joined.split() if i not in stop])
    normalized = stopfree2.split()
    return normalized


pd.options.display.max_colwidth = 500
ourdata["cleantext"] = ourdata["text"].apply(clean)

print (ourdata["cleantext"])


dictionary = corpora.Dictionary(ourdata["cleantext"])
doc_term_matrix = [dictionary.doc2bow(item) for item in ourdata["cleantext"]]


choice = input("LSI or LDA?")


if choice == "LDA":
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(doc_term_matrix, num_topics=5, id2word = dictionary, passes=50)
    ouroutput = ldamodel.print_topics(num_topics=5, num_words=4)

elif choice == "LSI":
    lsi = models.LsiModel(doc_term_matrix, num_topics=5, id2word=dictionary)
    ouroutput = lsi.print_topics(num_topics=5, num_words = 4)

else:
    print("not defined")
    



print(ouroutput)

listforplot = [list(i) for i in ouroutput]
print (listforplot)

topicnos = []
wordsfornew = []


for i in listforplot:
    newlabel = "Topic " + str(i[0] + 1)
    words = str(i[1])
    wordsfornew.append(words)
    topicnos.append(newlabel)



modelres = OrderedDict([('Topic Number',topicnos),
                     ('Words', wordsfornew)])

newdf = pd.DataFrame.from_dict(modelres)

print (newdf)
                     

from plotly import figure_factory as ff
table = ff.create_table(newdf)
plotly.offline.plot(table, filename='LITERATURETOPICMODELING.html')


