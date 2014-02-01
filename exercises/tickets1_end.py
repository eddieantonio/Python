num_tickets = 8

tickets_requested = raw_input("How many tickets do you want?\n")
tickets_requested = int(tickets_requested)

print "You've asked for {} ticket(s)".format(tickets_requested)
# deduct the tickets sold from available tickets
num_tickets = num_tickets - tickets_requested

#the number of remaining tickets
print "There are {} ticket(s) left".format(num_tickets)