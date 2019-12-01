import nltk
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
import numpy as np
import random
import string
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances
from shubham_training_set import training_data

##Functions##

def byes(user):
    for word in user:
        if word.lower() in bye:
            flag=False
            return random.choice(bye)

def LemNormalize(raw):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    tokens = nltk.word_tokenize(raw.translate(remove_punct_dict))
    tokens=[lemmer.lemmatize(token) for token in tokens]
    return tokens

def greeting(sentence):
    for word in sentence:
        if word.lower() in greet_in:
            return random.choice(greet_resp)

def tokenize(sentence):
    word_tokens=nltk.word_tokenize(sentence)
    return word_tokens

def remove_stop_words(sentence):
    stop_words=set(stopwords.words("english"))
    filtered_sent=[]
    for w in sentence:
        if w not in stop_words:
            filtered_sent.append(w)
    return filtered_sent

def greeting(sentence):
    for word in sentence:
        if word.lower() in greet_in:
            return random.choice(greet_resp)

def response(new_sent):
    sent.insert(0,new_sent)
    vectorizer=TfidfVectorizer()
    features=vectorizer.fit_transform(sent).todense()
    score=[]
    k=0
    for f in features:
        score.append((euclidean_distances(features[0],f)[0][0]))
        if(k==1):
            x=k
        if(score[k]==0 and k!=0):
            x=k
            break
        if(k>1):
            if(score[k]<score[x]):
                x=k
        k=k+1
    sent.remove(new_sent)
    return dic2[x-1]

##Initializations and Declarations##

lemmer=WordNetLemmatizer()
greet_in=("hello", "hi", "greetings", "sup", "what's up","hey","whatsupp")
greet_resp = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]
flag=True
dic1={}
dic2={}
sent=[]
sent_str=''

##Processing Data Set##

for i in range(0,68):
    dic2[i]=training_data[i]['class']

for i in range(0,68):
    dic1[i]=training_data[i]['sentence']
    sent.append(dic1[i])
    sent_str=sent_str+" "+dic1[i]

##Ready to talk##
    
print("Bot: Let's talk")

while(flag==True):
    user_resp=input("You: ")
    user_resp=user_resp.lower()
    user=LemNormalize(user_resp)
    if 'bye' in user:
        flag=False
        print("Bot: Bye! Take Care.")
    else:
        if 'thank' in user:
            flag=False
            print("Bot: You are welcome!")
        else:
            if(greeting(user)!=None):
                print("Bot: "+greeting(user))
            else:
                print("Bot: ", end="")
                print(response(user_resp))
