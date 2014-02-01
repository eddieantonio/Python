num_tickets = 8

tickets_requested = raw_input("How many tickets do you want?\n")
tickets_requested = int(tickets_requested)

print "You've asked for {} ticket(s)".format(tickets_requested)
# deduct the tickets sold from available tickets 
if tickets_requested > num_tickets:
    print "We're sorry. We don't have that many tickets"
else:
    num_tickets = num_tickets - tickets_requested
    print "Purchase successful"

#the number of remaining tickets
print "There are {} ticket(s) left".format(num_tickets)