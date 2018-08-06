# There are at least 10 "mistakes" in this Hangman game
# These could include syntax errors, logical errors, spelling errors...
# Find the mistakes and fix the game!
#
# STRETCH GOAL: If you fix all the errors, can you find a way to improve 
# it? Add a cheat code, more error handling, chose randomly
# from a set of win/loss messages...basically, make it better!
import random
# Initial setup
bodies = [ " ------\n |    |\n |    O\n |\n |\n |\n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |\n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \n |\n |\n---", 
" ------\n |    |\n |    O\n |    |\n |    |\n |   / \ \n |\n |\n---", 
" ------\n |    |\n |    O\n |   \|\n |    |\n |   / \ \n |\n |\n---",
" ------\n |    |\n |  O\n |   \|/\n |    |\n |   / \ \n |\n |\n---" ]
strikes = 0
words = [None]
file = open("words.txt", "r")
for line in file:
    words.append(line)
file.close()
target_word = words[random.randint(0, len(words))]
letters_left = len(targetWord)-1
length = len(targetWord)-1
cur_word = "_" * length
alphabet = [chr(65+x) for x in range(0, 26) ]

# Draw body based on # of incorrect guesses
def drawBody():
    print(bodies[strikes])

# Replace blanks with correctly guessed letters
def fillLetters( letter ):
    for i in range(len(targetWord)-1):
        if( targetWord[i : i+1]) == letter:
            global cur_word
            cur_word = cur_word[0: i] + letter + cur_word[i: ]
            global letters_left
            letters_left -= 1

# Add spaces when displaying letters / blanks for readability
def printWord( word ):
    prnt_word = ""
    for letter in word:
        prnt_word += letter + " "
    print(prnt_word)

# Begin game
print( "Welcome to Hangmn!" )
printWord(cur_word)
drawBody()
print("Letters left:")
printWord(alphabet)

# Gameplay loop
while strikes < 5 and letters_left > 0:
    letter = input("\nPlease guess a letter...")
    if letter in targetWord:
        print("Great!")
        fillLetters(letter)
    else:
        strikes += 1
        print( str(strikes) + " / 5 strikes" )
    printWord(curWord)
    drawBody()
    alphabet.remove(letter.upper())
    print("Letters left:")
    printWord(alphabet)

# Game over, print outcome
if lettersLeft < 0:
    print("YOU WIN!!")
else:
    print("YOU LOSE...word was " + targetWord)