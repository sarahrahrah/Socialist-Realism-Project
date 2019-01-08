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

for dirpath, dirnames, filenames in os.walk("banned_lit_corpus"):
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
 #           bannedorsoclit.append("banned_literature")
            bannedorsoclit.append("0")


for dirpath, dirnames, filenames in os.walk("socialist_realism_corpus"):
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
 #           bannedorsoclit.append("socialist_realism")
            bannedorsoclit.append("1")


newdataframe = pd.DataFrame(OrderedDict({
        "source": sourcelist,
        "title": titlelist,
        "date": datelist,
        "text": textlist,
        "bannedorsoclit": bannedorsoclit
    }))

newdataframe.to_csv('data_for_log_reg_large_chunks.csv', index=False)

print ("The _______________________.csv file is now created.")

