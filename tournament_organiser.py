# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested atm, losers bracket not functional yet)
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

initial_match_list = []
initial_matches_count = round(player_count / 2)
s = 0
e = player_count - 1
for n in range(initial_matches_count):
    # currently matches 1 vs last and goes inward, is this ideal?
    initial_match_list.append([player_names[int(s)], player_names[int(e-s)]])
    s += 1

print("Initial matches: " + str(initial_match_list))

winners_match_list = initial_match_list

# for debug
winners_match_list = [["John", "Joe"], ["Todd", "Tess"], ["Karen", "Katarina"], ["Elizabeth", "Edward"]]

while match_count > 0:
    print("DEBUG: winners_match_list = " + str(winners_match_list))
    print("DEBUG: winners_match_list[0] = " + str(winners_match_list[0]))
    while len(winners_match_list[0]) > 1:
    # need to change winners_match_list to be a list of paired players rather than just a list of players
        losers_match_list = []
        new_losers_match = []
        for n in winners_match_list:
            if len(new_losers_match) % 2 == 0 and len(new_losers_match) != 0:
                losers_match_list.append(new_losers_match)
                new_losers_match = []
                print("DEBUG: losers_match_list = " + str(losers_match_list))
            # input loser right now, change to winner later
            print("DEBUG: n[0] = " + str(n[0]))
            print("DEBUG: n[1] = " + str(n[1]))
            new_loser = int(input("Please enter _loser_ of " + str(n) + " (1/2): 1) " + str(n[0]) + " or 2) " + str(n[1]) + " "))
            print("DEBUG: n[0] = " + str(n[0]))
            print("DEBUG: n[1] = " + str(n[1]))
            if new_loser == 1:
                new_losers_match.append(n[0])
                print("DEBUG: new_losers_match = " + str(new_losers_match))
                n.remove(n[0])
            elif new_loser == 2:
                new_losers_match.append(n[1])
                print("DEBUG: new_losers_match = " + str(new_losers_match))
                n.remove(n[1])
            else:
                print("Invalid entry.")
                break
            match_count -= 1
            print("DEBUG: match_count = " + str(match_count))
        if len(winners_match_list[0]) == 1 and len(winners_match_list) == 1:
            print(str((winners_match_list[0])[0]) + " reaches GF! Now to face off against the winner of the losers' bracket!")
            print("DEBUG: Setting match count to zero")
            match_count = 0
        #change format of winners_match_list here
        elif len(winners_match_list[0]) == 1 and len(winners_match_list) != 1:
            win_while_count = 0 # debug
            while len(winners_match_list[0]) != 2:
                print("DEBUG: winners_match_list = " + str(winners_match_list))
                # inconsistent pruning of winners list (individuals are left as lists until this step, potentially can be improved)
                winners_match_list.append([(winners_match_list[0])[0], (winners_match_list[1])[0]])
                winners_match_list.remove(winners_match_list[1])
                winners_match_list.remove(winners_match_list[0])
        else:
            print("DEBUG: ERROR!")

print("DEBUG: END")
