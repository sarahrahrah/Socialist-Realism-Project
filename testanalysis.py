import numpy as np 
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

import plotly
import string
from plotly.graph_objs import Scatter, Layout


acc = []

df = pd.read_csv("DATAFORANALYSIS.csv")
y = df['bannedorsoclit']


testtext = open("testtext.txt", "r")
stringtext = testtext.read().replace('\n', '')
print (stringtext)

d = {"text":stringtext}
print (d)
testtextdf = pd.DataFrame([d], columns=d.keys())
print (testtextdf)


stemmer = SnowballStemmer("russian")
stop = set(stopwords.words('russian'))
otherstopwords = ["это","да","наш","сво","одн","говор","сказа","нам","—","котор","мо","очен","эт","теб"]
otherstop = set(otherstopwords)
stop.update(otherstop)
exclude = set(string.punctuation)

 
def clean(doc):
    nostop = " ".join([i for i in doc.lower().split() if i not in stop])
    nopunc = ''.join(ch for ch in nostop if ch not in exclude)
    stemmed = " ".join([stemmer.stem(word) for word in nopunc.split()])
    normalized = " ".join([i for i in stemmed.split() if i not in stop]) 
    return normalized


df["text"] = df["text"].apply(clean)
testtextdf["text"] = testtextdf["text"].apply(clean)


count_vectorizer = CountVectorizer(stop_words=None)
count_train = count_vectorizer.fit_transform(df["text"].values)
count_test = count_vectorizer.transform(testtextdf["text"].values)
runb_classifier = MultinomialNB(alpha=1.0, fit_prior=False, class_prior=None)

runb_classifier.fit(count_train, y)

pred = runb_classifier.predict(count_test)

print ("predicted value: " + pred)


