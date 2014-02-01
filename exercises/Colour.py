fav = raw_input('What is your favourite colour?\n')

fav_lower = fav.lower()

if fav_lower == 'green':
    print 'I like turtles'
elif fav_lower == 'blue':
    print 'Like the sky'
elif fav_lower == 'purple':
    print 'My favourite ice cream when I was young was called Purple People Eater'
else:
    print "{} is my favourite too.".format(fav)