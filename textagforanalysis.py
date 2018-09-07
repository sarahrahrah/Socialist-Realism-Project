import os
import numpy as np
import pandas as pd
from collections import OrderedDict, Counter

authorlist = []
titlelist = []
datelist = []
englishmetadatalist = []
sourcelist = []
textlist = []
bannedorsoclit = []


banned_fn = []
socrec_fn = []

for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/banned_lit_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            banned_fn.append(filename.split('_')[0])
least_common = Counter(banned_fn).most_common()[-1]
file_numb = list(least_common)[1]

banned_fn = []
for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/banned_lit_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            fn = filename.split('_')[0]
            banned_fn.append(fn)
            count = Counter(banned_fn).most_common()
            y = dict(count)
            if y[fn] < file_numb:
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
                bannedorsoclit.append("banned_literature")


for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/sr_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            socrec_fn.append(filename.split('_')[0])
least_common = Counter(socrec_fn).most_common()[-1]
file_numb = list(least_common)[1]

socrec_fn = []
for dirpath, dirnames, filenames in os.walk("preliminary_corpus_files_chunked/sr_corpus"):
    for filename in filenames:
        if filename != ".DS_Store":
            fn = filename.split('_')[0]
            socrec_fn.append(fn)
            count = Counter(socrec_fn).most_common()
            y = dict(count)
            if y[fn] < file_numb:
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
                bannedorsoclit.append("socialist_realism")


newdataframe = pd.DataFrame(OrderedDict({
        "source": sourcelist,
        "title": titlelist,
        "date": datelist,
        "text": textlist,
        "bannedorsoclit": bannedorsoclit
    }))

newdataframe.to_csv('DATAFORANALYSIS.csv', index=False)

print ("The DATAFORANALYSIS.csv file is now created.")

