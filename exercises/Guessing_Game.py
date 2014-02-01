from random import randint
x = randint(1,10)
print "I'm thinking of a number between 1 and 10"

correct = False

while not correct:
    guess = raw_input("Guess the number\n")
    guess = int(guess)
    if guess > x:
        print 'Too high'
    elif guess < x:
        print 'Too low'
    else:
        print "You're right!"
        correct = True