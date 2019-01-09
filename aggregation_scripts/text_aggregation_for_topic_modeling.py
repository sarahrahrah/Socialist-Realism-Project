import os
import numpy as np
import pandas as pd
from collections import OrderedDict

namelist = []
titlelist = []
datelist = []
englishmetadatalist = []
sourcelist = []
textlist = []

for dirpath, dirnames, filenames in os.walk("/Users/sarahmceleney/Desktop/socialist-realism-project-cleaner/corpus_files_chunked/socreal_files_chunked_smaller"):
    for filename in filenames:
        if filename != ".DS_Store":
            z = os.path.join(dirpath, filename)
            y = open(z, 'rb')
            print (filename)
            data = y.read().decode('utf8', 'ignore')
            name = data.split("***")[0]
            namelist.append(name)
            title = data.split("***")[1]
            titlelist.append(title)
            date = data.split("***")[2]
            datelist.append(date)
            englishmetadata = data.split("***")[3]
            englishmetadatalist.append(englishmetadata)           
            source = data.split("***")[4]
            sourcelist.append(source)
            text = data.split("***")[5]
            textlist.append(text)

newdataframe = pd.DataFrame(OrderedDict({
        
        "title": titlelist,
        "name": namelist,
        "date": datelist,
        "english metadata" : englishmetadatalist,
        "source": sourcelist,
        "text": textlist,
    }))

newdataframe.to_csv('socreal_files_chunked_smaller.csv', index=False)

print ("The ____________________.csv file is now created.")





