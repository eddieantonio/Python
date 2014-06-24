import random


HANGMAN = [

""""
------
|    |
|
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|   -+-
|
|
|
|
|
------
""",
""""
------
|    |
|    0
|  /-+-
|
|
|
|
|
------
""",

""""
------
|    |
|    0
|  /-+-/
|    |
|    
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   /
|
|
------
""",
""""
------
|    |
|    0
|  /-+-/
|    |
|    | 
|   / \\
|
|
------
"""
]


MAX_WRONG = len(HANGMAN) - 1

WORDS = ["ladies", "hello", "you", "fun", "code", "python"]


#Generate a random word from our list of words
word = random.choice(WORDS)

#Create a string that has one dash for each letter in the secret word
so_far = "-"*len(word)

#Create a variable to store the number of wrong guesses player has made
wrong = 0

#Create a list to store all the letters used
used = []


print "Welcome to Hangman. Good luck!"


while wrong < MAX_WRONG and so_far != word:
    print HANGMAN[wrong]

    guess = raw_input("Enter your guess: ")
    guess = guess.lower()

    used.append(guess)

    if guess in word:
		print "Yes! {0} is in the word".format(guess)

		new = ""

		for i in range(0, len(word)):
			if guess == word[i]:
				new = new + guess
			else:
				new = new + so_far[i]
		
		so_far = new

    else:
        print "Sorry {0} is NOT in the word.".format(guess)
        wrong += 1

    print "\nSo far, the word is: {0}".format(so_far)
    print "\nYou've used the following letters:\n", used


if wrong == MAX_WRONG:
	print HANGMAN[wrong]
	print "You've been hanged!"

else:
	print "You guessed it!"


print "The word was {0}".format(word)




