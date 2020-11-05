import random

print('Welcome to Python Hangman!')
print()

with open ('words.txt', 'r') as f:
    words = f.read().splitlines()
    word = (random.choice(words))
    print('The word your are trying to guess is', len(word), 'letters long you have 10 guesses')
    
guesses = 10
output = ['_'] * len(word)
ln = len(word)
correct = 0

# function to print the output list
def print_output():
    print()
    print (''.join([x+" " for x in output]))

while guesses != 0:
    print_output()
    letter = input('Please guess a letter? ')
    if letter in word:
        print('Correct {} is in the word'.format(letter))
        correct += 1
        for i,x in enumerate(word):
            if x is letter:
                output[i] = letter
        if correct == ln:
            print("Congratulations! you win.\n The word was {}".format(word))
            break
    else:
        print('Incorrect {} is not in the word'.format(letter))
        guesses = guesses - 1
        print('You have', guesses, 'remaining guesses')
        print()
        if guesses == 0:
            print('You loose, please try again. The word you was guessing was', word)

