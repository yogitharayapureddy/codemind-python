sentence = input()
longest = max(sentence.split(), key=len)
print(len(longest))