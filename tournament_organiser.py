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

print("Players: " + str(player_names))

match_count = (player_count - 1) * 2 + 1

print ("Match count: " + str(match_count))

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

initial_match_list = []
initial_matches_count = round(player_count / 2)
s = 0
e = player_count - 1
for n in range(initial_matches_count):
    # currently matches 1 vs last and goes inward
    initial_match_list.append([player_names[int(s)], player_names[int(e-s)]])
    s += 1

print("Initial matches: " + str(initial_match_list))

winners_match_list = initial_match_list

while match_count > 0:
    losers_match_list = []
    for n in winners_match_list:
        # input loser right now, change to winner later
        new_loser = int(input("Please enter _loser_ of " + str(n) + "(1/2): 1: " + str.(n[0]) + " or 2: " + str.(n[1])))
        new_losers_match = []
        if new_loser == 1:
            n.remove(n[0])
            new_losers_match.append(n[0])
        elif new_loser == 2:
            n.remove(n[1])
            new_losers_match.append(n[1])
        else:
            print "Invalid entry."
            continue
        if new_losers_match.count() % 2 == 0:
            losers_match_list.append(new_losers_match)
        match_count -= 1
# at this point winners match list is still a list of lists with single players in each
