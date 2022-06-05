from random import choice

#All possible lottery entries
options = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']

#Initial lottery list
winning_ticket = []

#Making ticket length 4
while len(winning_ticket) < 4:
	#Selecting random winning number
	value_a = choice(options)

	#Confirms random number only appears in ticket once and adds value to value_a
	if value_a not in winning_ticket:
		winning_ticket.append(value_a)


print(f'Winning Ticket: {winning_ticket}')

