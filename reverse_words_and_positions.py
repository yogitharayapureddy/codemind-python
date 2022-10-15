def reverseWordSentence(Sentence):
    words = Sentence.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
    return newSentence
Sentence = input()
string=reverseWordSentence(Sentence)
s = string.split()[::-1]
l = []
for i in s:
    l.append(i)
print(" ".join(l))