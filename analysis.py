import numpy as np 
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from sklearn.utils import shuffle


import plotly
import string
from plotly.graph_objs import Scatter, Layout
from collections import OrderedDict


acc = []

df = pd.read_csv("DATAFORANALYSIS.csv")
df = shuffle(df)

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

count_vectorizer = CountVectorizer(stop_words=None)
# count_vectorizer = TfidfVectorizer()
features = count_vectorizer.fit_transform(
    df['text'])

features_nd = features.toarray()

X_train, X_test, y_train, y_test = train_test_split(
                                             features_nd[0:len(df['text'])], y, 
                                             test_size=0.4, 
                                             random_state=53)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

# count_train = count_vectorizer.fit_transform(X_train.values)
# count_test = count_vectorizer.transform(X_test.values)

from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)
y_pred = log_model.predict(X_test)
print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(log_model.score(X_test, y_test)))

from sklearn import model_selection
kfold = model_selection.KFold(n_splits=10, random_state=7)
modelCV = LogisticRegression()
scoring = 'accuracy'
results = model_selection.cross_val_score(modelCV, X_train, y_train, cv=kfold, scoring=scoring)
print("10-fold cross validation average accuracy: %.3f" % (results.mean()))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print('confusion_matrix', confusion_matrix)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))

# runb_classifier = MultinomialNB(alpha=1.0, fit_prior=False, class_prior=None)



# runb_classifier.fit(count_train, y_train)
# pred = runb_classifier.predict(count_test)
# russcore = metrics.accuracy_score(y_test, pred)
# cm = metrics.confusion_matrix(y_test, pred, labels=[1, 0])



# cv_scores = cross_val_score(runb_classifier,count_train, y_train, cv=5)
# print(cv_scores)
# print("Average 5-Fold CV Score for testing data: {}".format(np.mean(cv_scores)))



# print(russcore)
# acc.append(russcore)

# print(cm)

# langs = ["SocReal/vsBannedLit"]
         
# results = OrderedDict([('Corpora',langs),
#                      ('Accuracy of Model (%)', acc)])
# newdf = pd.DataFrame.from_dict(results)


# def print_top10(vectorizer, clf, class_labels):
#     """Prints features with the highest coefficient values, for the positive case"""
#     feature_names = vectorizer.get_feature_names()
#     topn_class1 = sorted(zip(clf.feature_count_[0], feature_names),reverse=True)[:100]
#     topn_class2 = sorted(zip(clf.feature_count_[1], feature_names),reverse=True)[:100]

#     print("Important words in banned lit")
#     for coef, feat in topn_class1:
#         print(class_labels[0], coef, feat)
#     print("-----------------------------------------")
#     print("Important words in socialist realism")
#     for coef, feat in topn_class2:
#         print(class_labels[1], coef, feat) 

    
#     print (class_labels)
        
#     for i, class_label in [enumerate(class_labels)]:
#         top10 = np.argsort(clf.coef_[0])[-10:]
#         print("%s: %s" % (class_label,
#               " ".join(feature_names[j] for j in top10)))
#         top100 = np.argsort(clf.coef_[0])[-100:]
#         print("%s: %s" % (class_label,
#               " ".join(feature_names[j] for j in top100)))


# print_top10(count_vectorizer, runb_classifier, runb_classifier.classes_)



# from plotly import figure_factory as ff
# table = ff.create_table(newdf)
# plotly.offline.plot(table, filename='MLRESULTSTABLE.html')




