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
from pymystem3 import Mystem
import re

# Import data from csv

litdata = pd.read_csv("LITERATURE.csv")
littext = litdata["text"]



# Create a column in the dataframe that is the literature minus
# all punctuation and stopwords

with open('NERoutput.txt') as fp:
    lines = fp.read().splitlines()

lines = [i.lower() for i in lines]
stop = list(stopwords.words('russian'))
stop.extend(['это', 'свой', 'то', ' '])

mystem = Mystem() 
exclude = list(string.punctuation)
exclude.extend(['--', '—', '«', '»'," -- ", "-" ,"-", "...", "…", " - ", " « ", "..", "``", "\"\"","\'\'"])


# Cleaning text



def losepunctuation(text):
    tokens = text.split(" ")
    tokens = [i.strip().lower() for i in tokens]
    tokens = [i for i in tokens if i not in exclude]
    tokens = [re.sub(r'[!|,|?|.|:|;]|\.{1,}$\)', "", item) for item in tokens]
    tokens = [i for i in tokens if i not in stop]
    tokens = [i for i in tokens if i not in lines]
    cleanedtext = " ".join(tokens)
    lemmatized = mystem.lemmatize(cleanedtext.lower())
    lemmatized = [i for i in lemmatized if i not in exclude]
    lemmatized = [i for i in lemmatized if i not in stop]
    lemmatized = [i for i in lemmatized if i not in lines]

    print (lemmatized)

    return lemmatized


litdata["cleanedtext"] = litdata["text"].apply(losepunctuation)

print (litdata["cleanedtext"])


#Topic Modeling 


dictionary = corpora.Dictionary(litdata["cleanedtext"] )
doc_term_matrix = [dictionary.doc2bow(item) for item in litdata["cleanedtext"] ]


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


