import random

#txt from - https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt
# Open the file in read mode
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = random.choice(words)

    # print random string
word_length = len(word)-1
gap = random.randint(0,word_length)
print(gap)
for n in range(0,word_length-1):
    print(n)
print(word)
