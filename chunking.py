
import nltk

z = "./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit.txt"




y = open(z, 'rb')

file = y.read().decode('utf8', 'ignore')

print (file)

print (type(file))

print (len(file))


tokens = nltk.word_tokenize(file)

for i in range(0, 8):
    chunk = str(i + 1) 
    if len(tokens) >= 5000:
        tokensarray = tokens[0:5000]
        joinedtokensarray = ' '.join(tokensarray)
        text_file = open("./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit-" + chunk + ".txt","w")
        text_file.write(joinedtokensarray)
        del tokens[0:5000]

    else:
        tokensarray = tokens
        joinedtokensarray = ' '.join(tokensarray)
        text_file = open("./preliminary_corpus_files_chunked/banned_lit_corpus/platonov_the-foundation-pit-" + chunk + ".txt","w")
        text_file.write(joinedtokensarray)



    
        
#    x = tokens[i]
    
    #array1.append(x)

#print (array)
    
