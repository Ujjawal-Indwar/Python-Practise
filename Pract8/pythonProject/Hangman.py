import random

#txt from - https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt
# Open the file in read mode
with open("MyFile.txt", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    word = random.choice(words)

    # print random string
word_length = len(word)
gap = random.randint(0,word_length)
print(word_length)
print(gap)
for n in range(0,word_length):
    print(end='_ ')

print()
print(word)
originalLetters = list(word)


#guess = ["_"]*word_length
guess = []
for _ in range(word_length):
    guess +="_"

print(guess)
print(originalLetters)

end_of_game = False

while not end_of_game:
    guessLetter = input(f'Guess an alphabet in this {word_length} letter word \n').lower()
    for pos in range(word_length):
        letter = originalLetters[pos]
        if (letter == guessLetter):
            guess[pos] = letter

    print(guess)

    if "_" not in guess:
        end_of_game = True
        print("You win")

# for i ,letter in enumerate(originalLetters):
#     if guessLetter==letter:
#         guess[i]=letter
#         print("yes")
#
#     else:
#        print("no")


