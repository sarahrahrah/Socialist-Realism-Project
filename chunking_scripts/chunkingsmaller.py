#If this doesn't work it's because there is a hidden .DS_Store file in the folder mucking things up

# new script makes 8 chunks max

# This pretty much does what you want, excluding metadata now.

# !~!~!~!~ Now just figure out how to deal with the metadata !~!~!~!~
# This will require some regex, surely 



import nltk
import math
import os

import re

for root, dirs, files in os.walk("preliminary_corpus_files/socialist_realism_corpus/"):  
    for filename in files:
        print(filename) 
        file = open(os.path.join(root, filename), 'r').read()
        print (file)

        tokens = nltk.word_tokenize(file)
        toklen =  len(tokens)


        length = toklen / 5000
        rounduplength = math.ceil(length)
        print (len(tokens))

# Instead of chunking length of each document, just go up to 8 chunks.  Thus, the if statement is kind of
#irrelevant, but oh well. Maybe fix this later. No its not irrelevant actually.  Added another if statement
# Fixed, this does the trick

 #      for i in range(0, rounduplength):
        for i in range (0, rounduplength):
            if i <= 8:
                chunk = str(i + 1)
                if chunk == 1:
                    tokensarray = tokens[0:5000]
                    joinedtokensarray = ' '.join(tokensarray)
                    text_file = open("newnewchunks/" + filename + chunk + ".txt","w")
                    text_file.write(joinedtokensarray)
                    del tokens[0:5000]
                
                elif len(tokens) >= 5000:
                    tokensarray = tokens[0:5000]
                    joinedtokensarray = ' '.join(tokensarray)
                    text_file = open("newnewchunks/" + filename + chunk + ".txt","w")
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
                    text_file = open("newnewchunks/"  + filename  + chunk + ".txt","w")
    #                text_file.write(" Фадеев, Александр Александрович *** Молодая гвардия " + chunk + " *** 1946 *** Aleksandr Fadeev, The Young Guard, 1946 *** http://lib.ru/RUSSLIT/FADEEW/mol_gwardiya.txt *** ")
                    match = re.findall(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}", file)
                    split = re.split(r"^((?:(?![*]{3})[\s\S])*[*]{3}(?:(?![*]{3})[\s\S])*)[*]{3}",file)
                    secondhalf = split[2]
                    newmatch = re.findall(r"([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)([*]{3}[\s\S]*?)", secondhalf)
                    joined = ' '.join(newmatch[0])
                    text_file.write(split[1] + " *** " + chunk + joined)
                    text_file.write(joinedtokensarray)

            else:
                break



#preliminary_corpus_files/socialist_realism_corpus/
