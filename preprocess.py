



import pickle
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words("english"))
stop_words.add('?')
stop_words.add('q.')
stop_words.add('a.')
stop_words.add('.')
stop_words.add('\'s')
stop_words.add(',')
stop_words.add(':')
stop_words.add('@')
stop_words.add('#')
#stop_words = set(stopwords)


def removestop(wordlist):
       
    ans = []
    for i in wordlist:
        if i not in stop_words:
            ans.append(i)
    return ans

def lemmatizefun(wordlist):
    le = WordNetLemmatizer()
    res = []
    for w in wordlist:
        #print(w)
        res.append(le.lemmatize(w))

    #print(res)
    return res    

listoffiles = ["loan_ques","netbank_ques","imd_ques","ppf_ques","travelcard_ques"]
listwrite =   ["loan_p","netbank_p","imd_p","ppf_p","travelcard_p"]

cnt = 0

for f in listoffiles:
    file = open(f,'rb')
    l = pickle.load(file)
    file.close()

    ans = []
    #print('sdfb')


    for item in l:
        #print(item)
        item = item.lower()
        tokenized = word_tokenize(item)
        wordlist = removestop(tokenized)
        wordlist = lemmatizefun(wordlist)
        wordlist = set(wordlist)
        ans.append(wordlist)

    fl = listwrite[cnt]
    cnt = cnt + 1
    file = open(fl,'wb')
    pickle.dump(ans,file)
    file.close()


    
    
    
