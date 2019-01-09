#If this doesn't work it's because there is a hidden .DS_Store file in the folder interfering with os.walk
# rm .DS_Store




import nltk
import math
import os

import re

for root, dirs, files in os.walk("/Users/sarahmceleney/Desktop/socialist-realism-project-cleaner/corpus_files/socialist_realism/"):  
    for filename in files:
        file = open(os.path.join(root, filename), 'r').read()

        tokens = nltk.word_tokenize(file)
        toklen =  len(tokens)


        length = toklen / 5000
        rounduplength = math.ceil(length)

        for i in range (0, rounduplength):
            if i <= 8:
                intchunk = i + 1
                chunk = str(i + 1)
                if intchunk == 1:
                    tokensarray = tokens[0:5000]
                    joinedtokensarray = ' '.join(tokensarray)
                    text_file = open("/Users/sarahmceleney/Desktop/socialist-realism-project-cleaner/test/" + filename + chunk + ".txt","w")
                    text_file.write(joinedtokensarray)
                    del tokens[0:5000]
                
                elif intchunk != 1 and len(tokens) >= 5000:
                    tokensarray = tokens[0:5000]
                    joinedtokensarray = ' '.join(tokensarray)
                    text_file = open("/Users/sarahmceleney/Desktop/socialist-realism-project-cleaner/test/" + filename + chunk + ".txt","w")
                    match = re.findall(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}", file)
                    split = re.split(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}",file)
                    secondhalf = split[2]
                    newmatch = re.findall(r"([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)", secondhalf)
                    joined = ' '.join(newmatch[0])
                    text_file.write(split[1] + " *** " +  chunk + joined)
                    text_file.write(joinedtokensarray)
                    del tokens[0:5000]

                else:
                    tokensarray = tokens
                    joinedtokensarray = ' '.join(tokensarray)
                    text_file = open("/Users/sarahmceleney/Desktop/socialist-realism-project-cleaner/test/"  + filename  + chunk + ".txt","w")
                    match = re.findall(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}", file)
                    split = re.split(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}",file)
                    secondhalf = split[2]
                    newmatch = re.findall(r"([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)", secondhalf)
                    joined = ' '.join(newmatch[0])
                    text_file.write(split[1] + " *** " + chunk + joined)
                    text_file.write(joinedtokensarray)

            else:
                break


