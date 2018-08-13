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
from collections import OrderedDict


acc = []

df = pd.read_csv("DATAFORANALYSIS.csv")
y = df['bannedorsoclit']

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

print (df["text"] )

X_train, X_test, y_train, y_test = train_test_split(
                                             df['text'], y, 
                                             test_size=0.3, 
                                             random_state=53)


count_vectorizer = CountVectorizer(stop_words=None)
count_train = count_vectorizer.fit_transform(X_train.values)
count_test = count_vectorizer.transform(X_test.values)
runb_classifier = MultinomialNB(alpha=1.0, fit_prior=False, class_prior=None)



runb_classifier.fit(count_train, y_train)
pred = runb_classifier.predict(count_test)
russcore = metrics.accuracy_score(y_test, pred)
cm = metrics.confusion_matrix(y_test, pred, labels=[1, 0])



cv_scores = cross_val_score(runb_classifier,count_train, y_train, cv=5)
print(cv_scores)
print("Average 5-Fold CV Score for testing data: {}".format(np.mean(cv_scores)))



print(russcore)
acc.append(russcore)

print(cm)

langs = ["SocReal/vsBannedLit"]
         
results = OrderedDict([('Corpora',langs),
                     ('Accuracy of Model (%)', acc)])
newdf = pd.DataFrame.from_dict(results)


def print_top10(vectorizer, clf, class_labels):
    """Prints features with the highest coefficient values, for the positive case"""
    feature_names = vectorizer.get_feature_names()
    for i, class_label in [enumerate(class_labels)]:
        top10 = np.argsort(clf.coef_[0])[-10:]
        print("%s: %s" % (class_label,
              " ".join(feature_names[j] for j in top10)))
        top100 = np.argsort(clf.coef_[0])[-100:]
        print("%s: %s" % (class_label,
              " ".join(feature_names[j] for j in top100)))
          

print_top10(count_vectorizer, runb_classifier, runb_classifier.classes_)



from plotly import figure_factory as ff
table = ff.create_table(newdf)
plotly.offline.plot(table, filename='MLRESULTSTABLE.html')




