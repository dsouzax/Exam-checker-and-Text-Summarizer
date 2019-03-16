import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import RegexpTokenizer
import heapq
from heapq import nlargest


f = open(os.path.expanduser('/Users/xavier/Desktop/news.txt'))
text = f.read()
print(text)
# f = open('/home/shambhavi/Desktop/hackathon/avengers1.txt','rU')
# text = f.read()
# text1 = text.split()
# docx = nltk.Text(text1)
print('\n\n')

sent_text = nltk.sent_tokenize(text)
print(sent_text)

print('\n\n')

# tokenized_word=word_tokenize(text)
# print(tokenized_word)

print('\n\n')

tokenizer = RegexpTokenizer(r'\w+')
result = tokenizer.tokenize(text)
print(result)

print('\n\n')

stoplist = stopwords.words('english')
#print(stoplist)

filtered_sent=[]
for word in result:
    word = word.lower()
    if word not in stoplist:
        filtered_sent.append(word)
#print("Tokenized Sentence:",sent_text)
print("Filtered Sentence:",filtered_sent)
print('\n\n')

fdist = nltk.FreqDist(filtered_sent)
mostCommon = fdist.most_common(1)
print(mostCommon)

print('\n\n')

ps = PorterStemmer()

freqTable = dict()
for word in filtered_sent:
    word = ps.stem(word)
    if word in stoplist:
        continue
    if word in freqTable:
        freqTable[word] = freqTable[word] + 1
    else:
        freqTable[word] = 1
print(freqTable)



v=freqTable.values()
x=max(v)
# print(x)

print('\n')


# Weight FREQ
weighted_freq = [p / x for p in v]
# print(weighted_freq)


print('\n')

# heaping
sentence_scores = {}
for sent in sent_text:
    for word in nltk.word_tokenize(sent.lower()):
        if word in freqTable.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = freqTable[word]
                else:
                    sentence_scores[sent] = sentence_scores[sent] + freqTable[word]
print(sentence_scores)

print('\n\n')


summary_sentences = nlargest(3, sentence_scores, key=None)

summary = ' '.join(summary_sentences)
print()
print(summary)