# simple tournament organiser (only double elim, single pool at the moment, only even players tested atm)
player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue

player_names = []

# currently seed position is stored in order in the list, no key-value pair
for n in range(player_count):
    player_names.append(input("Please enter seed %d name: " % (n + 1)))

# needs better formatting
print("Players: " + str(player_names))

# formula for double elim
match_count = (player_count - 1) * 2 + 1

# to assign initial matches
next_match_list = []
initial_matches_count = round(player_count / 2)
# iterates through players without for loop
s = 0
e = player_count - 1
for n in range(initial_matches_count):
    # currently matches 1 vs last and goes inward, is this ideal?
    next_match_list.append([player_names[int(s)], player_names[int(e-s)]])
    s += 1

# needs better formatting
print("Initial matches: " + str(next_match_list))

# establish lists for use below
winners_match_list = []
losers_match_list = []

# initial matches inputs
while len(winners_match_list) != player_count / 2: # need to fix this for odd number of players
    for n in next_match_list:
        # for each pairing in winners_match_list, the for loop asks for the victor
        new_winner = int(input("Please use 1) or 2) to select winner of " + str(n[0]) + " vs " + str(n[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(n[0])
            winners_match_list.append(n[1])
        elif new_winner == 1:
            losers_match_list.append(n[1])
            winners_match_list.append(n[0])
        # haven't tested the else
        else:
            print("Invalid entry.")
            break
        match_count -= 1 # reduce match count after declaration of winner

print("Initial round winners: " + str(winners_match_list))
print("Initial round losers:  " + str(losers_match_list))

next_match_list = []

# losers play each other
s = 0
e = len(losers_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
    match_count -= 1
    s += 1

print("DEBUG: losers_match_list = " + str(losers_match_list))

# winners play each other
s = 0
e = len(winners_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(winners_match_list[0])
        winners_match_list.append(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(winners_match_list[1])
        winners_match_list.append(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
    match_count -= 1
    s += 1

print("DEBUG: winners_match_list = " + str(winners_match_list))
print("DEBUG: losers_match_list = " + str(losers_match_list))

# losers again (this stuff really should all be one big loop)
# the below is not ideal
temp_losers_match_list = losers_match_list
losers_match_list = []
s = 0
e = len(temp_losers_match_list) / 2
while s != e:
    losers_match_list.append(temp_losers_match_list[s])
    losers_match_list.append(temp_losers_match_list[s+2])
    s += 1

print("DEBUG: losers_match_list = " + str(losers_match_list))

s = 0
e = len(losers_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
    match_count -= 1
    s += 1

print("DEBUG: losers_match_list = " + str(losers_match_list))

# winners again
s = 0
e = len(winners_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(winners_match_list[0])
        winners_match_list.append(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(winners_match_list[1])
        winners_match_list.append(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
    match_count -= 1
    s += 1

print("DEBUG: winners_match_list = " + str(winners_match_list))
print("DEBUG: losers_match_list = " + str(losers_match_list))

if len(losers_match_list) % 2 != 0:
    losers_waiting = []
    losers_waiting.append(losers_match_list[-1])
    losers_match_list.remove(losers_match_list[-1])

# last 2 losers play
s = 0
e = len(losers_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
    match_count -= 1
    s += 1
print("DEBUG: losers_match_list = " + str(losers_match_list))

if len(losers_match_list) == len(losers_waiting):
    losers_match_list.append(losers_waiting[-1])
    losers_waiting.remove(losers_waiting[-1])

# losers final
s = 0
e = len(losers_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(losers_match_list[0])
        losers_match_list.remove(losers_match_list[1])
        losers_match_list.remove(losers_match_list[0])
    match_count -= 1
    s += 1
print("DEBUG: losers_match_list = " + str(losers_match_list))

if len(losers_match_list) == 1 and len(losers_waiting) == 0:
    winners_match_list.append(losers_match_list[0])

# grand final
s = 0
e = len(winners_match_list) / 2

while s != e:
    new_winner = int(input("Please use 1) or 2) to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
    if new_winner == 2:
        losers_match_list.append(winners_match_list[0])
        winners_match_list.append(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
    elif new_winner == 1:
        losers_match_list.append(winners_match_list[1])
        winners_match_list.append(winners_match_list[0])
        winners_match_list.remove(winners_match_list[1])
        winners_match_list.remove(winners_match_list[0])
    match_count -= 1
    s += 1

print("DEBUG: winners_match_list = " + str(winners_match_list))
print("DEBUG: losers_match_list = " + str(losers_match_list))

# if match_count == 0:
if len(winners_match_list) == 1:
    print("The winner is " + str(winners_match_list[0]) +"!")


print("DEBUG: Overhaul done up to here.")
"""
# losers' match inputs
print("DEBUG: losers_match_list = " + str(losers_match_list))
    while len(losers_match_list[0]) > 1: # while losers_match_list's initial list is more than 1 player
        for n in losers_match_list:
            # after winners' matches are played, losers_match_list is initially half the player count minus 1
            # this separates the players at the end as they shouldn't be paired against one another
            if len(losers_match_list) == player_count / 2 - 1:
                # cut last player from last (incorrect) pairing
                cut2 = (losers_match_list[-1])[-1]
                # as above but first player
                cut3 = (losers_match_list[-1])[0]
                # remove erroneous pairing
                losers_match_list.remove(losers_match_list[-1])
                # paste players back as separate
                losers_match_list.append([cut3])
                losers_match_list.append([cut2])



                new_winner = int(input("Please enter winner of " + str(n) + " (1/2): 1) " + str(n[0]) + " or 2) " + str(n[-1]) + " "))
                if new_winner == 2:
                    print(losers_match_list) # debug
                    n.remove(n[0])
                    print(losers_match_list) # debug
                elif new_winner == 1:
                    print(losers_match_list) # debug
                    n.remove(n[-1])
                    print(losers_match_list) # debug
                else:
                    print("Invalid entry.")
                    break
            else:
                # error here - 8, 2, 6, 4 - 8 should play 2 and 6 should play 4
                new_winner = int(input("Please enter winner of " + str(n) + " (1/2): 1) " + str(n[0]) + " or 2) " + str(n[1]) + " "))
                if new_winner == 2:
                    print(losers_match_list) # debug
                    n.remove(n[0])
                    print(losers_match_list) # debug
                elif new_winner == 1:
                    print(losers_match_list) # debug
                    n.remove(n[1])
                    print(losers_match_list) # debug
                else:
                    print("Invalid entry.")
                    break
            match_count -= 1
        if len(losers_match_list[0]) == 1 and len(losers_match_list) == 1:
            print(str((losers_match_list[0])[0]) + " reaches GF! Now to face off against the winner of the winners' bracket!")
        # problem is with the below is after the first round of losers, 'todd' and 'elizabeth' shouldn't play each other
        # one should play 'joe' and one should play 'katarina'
        # winners of those matches play each other as normal
        # then the winner plays 'karen' to get into the grand final
        # preparing for 8 players with the below
        elif len(losers_match_list[0]) == 1 and len(losers_match_list) != 1:
            while len(losers_match_list[0]) != 2:
                # inconsistent pruning of winners list (individuals are left as lists until this step, potentially can be improved)
                losers_match_list.append([(losers_match_list[0])[0], (losers_match_list[1])[0]])
                losers_match_list.remove(losers_match_list[1])
                losers_match_list.remove(losers_match_list[0])
        else:
                print("ERROR!")
print("END")
"""
