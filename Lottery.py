from random import choice
#how hard to win
#Loop that pulls numbers until your ticket wins
#print message saying how long it took for ticket to win
#All possible lottery entries
def generate_ticket():
	options = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']
	ticket = []
	while len(ticket) < 4:
		value_a = choice(options)

		if value_a not in ticket:
			ticket.append(value_a)
	
	return ticket

winning_ticket = generate_ticket()
print(winning_ticket)

status = True
count = 0

while True:
	count += 1
	your_ticket = generate_ticket()
	if your_ticket != winning_ticket:
		print(f'{your_ticket} {winning_ticket}')
		print("Your ticket was not a winner!")
	else:
		print(f'\nTicket # : {your_ticket} winning_ticket #: {winning_ticket}')
		print("You won the lottery!")
		print(f" It took you {count} tries!")
		break










