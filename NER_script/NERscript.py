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

# Import data from .csv

litdata = pd.read_csv("LITERATURE.csv")
littext = litdata["text"]


# Creat a list with named PER entities from the
# litdata["text"] COLUMN

import spacy
nlp = spacy.load('xx_ent_wiki_sm')

litdatalist = littext.tolist()

perlist = []

for i in range(0, len(litdatalist)):
    textforner = nlp(litdatalist[i])
    for ent in textforner.ents:
        print(ent.text, ent.label_)
        if ent.label_ == "PER":
            perlist.append(ent.text)


print (perlist)
perlist = [item for item in perlist if perlist.count(item) >= 10]
perlist = set(perlist)
print (perlist)


filewithwords = open("newfilewithwords.txt","w")
filewithwords.write('\n'.join(perlist))
filewithwords.close()

