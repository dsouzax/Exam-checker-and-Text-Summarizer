def FunctionAlgo():
    import nltk
    import os
    from nltk.stem import PorterStemmer
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    from heapq import nlargest
    from difflib import SequenceMatcher

    def readFile():
        f = open(os.path.expanduser('/home/kadmin/PycharmProjects/p1/exp1.txt'))
        text = f.read()
        return text

    def readAns():
        f = open(os.path.expanduser('/home/kadmin/PycharmProjects/p1/exp2.txt'))
        text = f.read()
        # print(text)
        return text

    def tokenizeSent(text):
        sent_text = nltk.sent_tokenize(text)
        return sent_text

    def filterText(text):
        tokenizer = RegexpTokenizer(r'\w+')
        result = tokenizer.tokenize(text)
        stoplist = stopwords.words('english')
        filtered_sent = []
        for w in result:
            w = w.lower()
            if w not in stoplist:
                filtered_sent.append(w)
        # print(filtered_sent)
        return filtered_sent

    def wordFreq(filtered_sent):
        stoplist = stopwords.words('english')
        fdist = nltk.FreqDist(filtered_sent)
        mostCommon = fdist.most_common(1)
        # print(mostCommon)
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
        # print(freqTable)
        return freqTable

    def scoreSent(sent_text, freqTable):
        sentence_scores = {}
        for sent in sent_text:
            for word in nltk.word_tokenize(sent.lower()):
                if word in freqTable.keys():
                    if len(sent.split(' ')) < 30:
                        if sent not in sentence_scores.keys():
                            sentence_scores[sent] = freqTable[word]
                        else:
                            sentence_scores[sent] = sentence_scores[sent] + freqTable[word]
        # print(sentence_scores)
        return sentence_scores

    def summFile(sentence_scores):
        summary_sentences = nlargest(3, sentence_scores, key=None)

        summary = ' '.join(summary_sentences)
        # print(summary)
        return summary

    # Answerkey
    fileContent = readFile()
    sent_token = tokenizeSent(fileContent)
    filteredContent = filterText(fileContent)
    wordFrequency = wordFreq(filteredContent)
    sent_score = scoreSent(sent_token, wordFrequency)
    summi = summFile(sent_score)
    print(summi)
    a = summi

    print()

    # Student answer
    fileContent = readAns()
    sent_token = tokenizeSent(fileContent)
    filteredContent = filterText(fileContent)
    wordFrequency = wordFreq(filteredContent)
    sent_score = scoreSent(sent_token, wordFrequency)
    doc2 = summFile(sent_score)
    print(doc2)
    b = doc2


    d = SequenceMatcher(None, a, b).ratio()
    d = d * 10

    if (d > 0.8):
        return("Grade A")

    elif (d < 0.8 and d > 0.7):
        return ("Grade B")

    elif (d < 0.7 and d > 0.6):
        return ("Grade C")

    elif (d < 0.6 and d > 0.5):
        return ("Grade D")

    else:
        return ("Fail")
