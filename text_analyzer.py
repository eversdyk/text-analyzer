import re
import string
def textcontent(filename):
    text=open(filename).read()
    words=text.translate(None, string.punctuation).lower().split()
    wordcount=len(words)
    sentencecount=len(re.findall("[.?!]", text))
    s=set(words)
    wordfreq={}
    for i in words:
        if i in wordfreq:
            wordfreq[i]+=1
        else:
            wordfreq[i]=1
    print("Total word count: %i" %(wordcount))
    print("Total unique words: %i" %(len(s)))
    print("Number of sentences: %i" %(sentencecount))
    print("Most frequently occurring word: '%s'" %(max(wordfreq, key=wordfreq.get)))

#tested with a passage from Lord of the Rings :)
textcontent("LOTR.txt")
