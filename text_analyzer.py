"""
The challenge is to create a text content analyzer. This is a tool used by writers to find statistics such as word and sentence count on essays or articles they are writing.
Write a Python program that analyzes input from a file and compiles statistics on it.
The program should output:
1. The total word count
2. The count of unique words
3. The number of sentences
Example output:

Total word count: 468
Unique words: 223
Sentences: 38
Brownie points will be awarded for the following extras:
1. The ability to calculate the average sentence length in words
2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)
3. A list of words used, in order of descending frequency
4. The ability to accept input from STDIN, or from a file specified on the command line.
"""
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

textcontent("LOTR.txt")
