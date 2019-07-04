import nltk
import numpy as np
import random
import string  # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


f = open('CN-Definitions.txt', 'r', errors='ignore')
raw = f.read()
raw = raw.lower()  # converts to lowercase

# nltk.download('punkt') # first-time use only
# nltk.download('wordnet') # first-time use only

sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()  # WordNet is an English Dictionary included in NLTK


def LemTokens(tokens):  # when passed a list of tokens will return a list of lemmatized tokens
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text): # takes a string and outputs the lemmatized lowercase list of words with removed punctuations
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


GREETING_INPUTS = ["hello", "hi", "greetings", "sup", "what's up", "hey", "salam"]
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "Hello! I am glad you are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)




def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response

flag=False

def getResponse(inputString):
    global flag
    if(flag == False):
        flag = True
        return("ROBO: My name is Robo. I will answer your queries about Computer Networks. If you want to exit, type Bye or Thanks!")
    else:
        user_response = inputString.lower()
        if(user_response!='bye'):
            if(user_response=='thanks' or user_response=='thank you' ):
                flag=False
                return("ROBO: You are welcome.. Goodbye")
            else:
                if(greeting(user_response)!=None):
                    return("ROBO: "+greeting(user_response))
                else:
                    return("ROBO: " + response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag=False
            return("ROBO: Bye! take care")

