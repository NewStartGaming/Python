from random import choice

#All possible lottery entries
lottery = [1,2,3,4,5,6,7,8,9,0,'a','b','c','d','e']

#Values for lottery
value_a = choice(lottery)
value_b = choice(lottery)
value_c = choice(lottery)
value_d = choice(lottery)
winning_ticket = f'Winning numbers:{value_a}{value_b}{value_c}{value_d}'

print(winning_ticket)

