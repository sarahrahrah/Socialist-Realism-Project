
import nltk
import math

z = "./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit.txt"




y = open(z, 'rb')

file = y.read().decode('utf8', 'ignore')

print (file)

print (type(file))

print (len(file))


tokens = nltk.word_tokenize(file)
toklen =  len(tokens)

length = toklen / 5000
rounduplength = math.ceil(length)
print (len(tokens))

for i in range(0, rounduplength):
    chunk = str(i + 1) 
    if len(tokens) >= 5000:
        tokensarray = tokens[0:5000]
        joinedtokensarray = ' '.join(tokensarray)
        text_file = open("./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit-" + chunk + ".txt","w")
        text_file.write("Платонов, Андрей Платонович *** Котлован " + chunk + "*** 1926-1928 *** Andrei Platonov, The Foundation Pit, 1930 *** https://ilibrary.ru/text/1010/index.html ***")
        text_file.write(joinedtokensarray)
        del tokens[0:5000]

    else:
        tokensarray = tokens
        joinedtokensarray = ' '.join(tokensarray)
        text_file = open("./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit-" + chunk + ".txt","w")
        text_file.write("Платонов, Андрей Платонович *** Котлован " + chunk + "*** 1926-1928 *** Andrei Platonov, The Foundation Pit, 1930 *** https://ilibrary.ru/text/1010/index.html ***")
        text_file.write(joinedtokensarray)
print (rounduplength)
        
#    x = tokens[i]
    
    #array1.append(x)

#print (array)
    
