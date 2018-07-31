import os
import numpy as np
import pandas as pd
from collections import OrderedDict

authorlist = []
titlelist = []
datelist = []
englishmetadatalist = []
sourcelist = []
textlist = []
bannedorsoclit = []

for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/banned_lit_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            z = os.path.join(dirpath, filename)
            y = open(z, 'rb')
            print (filename)
            data = y.read().decode('utf8', 'ignore')
            author = data.split("***")[0]
            authorlist.append(author)
            title = data.split("***")[1]
            titlelist.append(title)
            date = data.split("***")[2]
            datelist.append(date)
            engmd = data.split("***")[3]
            englishmetadatalist.append(engmd)
            source = data.split("***")[4]
            sourcelist.append(source)
            text = data.split("***")[5]
            textlist.append(text)
            bannedorsoclit.append(0)


for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/sr_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            z = os.path.join(dirpath, filename)
            y = open(z, 'rb')
            print (filename)
            data = y.read().decode('utf8', 'ignore')
            author = data.split("***")[0]
            authorlist.append(author)
            title = data.split("***")[1]
            titlelist.append(title)
            date = data.split("***")[2]
            datelist.append(date)
            engmd = data.split("***")[3]
            englishmetadatalist.append(engmd)
            source = data.split("***")[4]
            sourcelist.append(source)
            text = data.split("***")[5]
            textlist.append(text)
            bannedorsoclit.append(1)


newdataframe = pd.DataFrame(OrderedDict({
        "source": sourcelist,
        "title": titlelist,
        "date": datelist,
        "text": textlist,
        "bannedorsoclit": bannedorsoclit
    }))

newdataframe.to_csv('DATAFORANALYSIS.csv', index=False)

print ("The DATAFORANALYSIS.csv file is now created.")

