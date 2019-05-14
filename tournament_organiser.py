# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested)
player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue

player_names = []

# currently seed position is stored in order in the list, no need to key-value pair
for n in range(player_count):
    player_names.append(input("Please enter seed %d name: " % (n + 1)))

print(player_names)

match_count = ( player_count - 1 ) * 2 + 1

print (match_count)

"""
8 player example
Winners
QF      SF      F       GF      GFR
-----------------------------------
A
        E
B
                G       H       I
C
        F
D

Losers
        QF      SF      F
-------------------------
J       L
                N       O
K       M

J and K are losers of A and B, L and M incorporate losers of E and F etc.
"""

# if player_count % 2 == 0: to use later

# need to create the following
# winners_dict = {[player_names[0], player_names[-1]], [player_names[0+1], player_names[second last]]} etc.)

winners_dict = {}

winners_start = player_count + ( player_count % 2 )
