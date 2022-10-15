def reverseWordSentence(s):
    words = s.split(" ")
    newWords = [word[::-1] for word in words]
    newSentence = " ".join(newWords)
 
    return newSentence
 

s = input()
print(reverseWordSentence(s))