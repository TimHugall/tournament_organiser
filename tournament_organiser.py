# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested atm)
player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue

init_match_list = []

# currently seed position is stored in order in the list, no key-value pair
for n in range(player_count):
    init_match_list.append(input("Please enter seed %d name: " % (n + 1)))

# needs better formatting
print("Players: " + str(init_match_list))

# formula for double elim
init_match_count = (player_count - 1) * 2 + 1
rem_match_count = initial_match_count
# establish lists for use below
losers_match_list = []
winners_match_list = []

# reserved section for matches in case of uneven number of players

# init matches - matches 1st seed vs 8th seed etc, not sure if this is the preferred method
print("Initial round")
s = 0
while rem_match_count != init_match_count / 2:
    new_winner = int(input("Please enter 1 or 2 to select winner of " + str(init_match_list[s]) + " vs " + str(init_match_list[-(s+1)]) + ": "))
    if new_winner == 1:
        winners_match_list.append(init_match_list[s])
        losers_match_list.append(init_match_list[-(s+1)])
    elif new_winner == 2:
        winners_match_list.append(init_match_list[-(s+1)])
        losers_match_list.append(init_match_list[s])
    rem_match_count -= 1
    s += 1

print("Winners: " + str(winners_match_list))
print("Losers: " + str(losers_match_list))

# winners and losers repeating matches
while rem_match_count > 1:
    # winners until GF
    s = 0
    while len(winners_match_list) > 1:
        print("Winners' round")
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[s]) + " vs " + str(winners_match_list[s+1]) + ": "))
        if new_winner == 1:
            losers_match_list.append(winners_match_list[s+1])
            winners_match_list.remove(winners_match_list[s+1])
            winners_match_list.append(s) # put winners at end again so order isn't disrupted - rebuilds list
            winners_match_list.remove(s) # remove winner from start so not cycled over
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        elif new_winner == 2:
            winners_match_list.append(s+1) # see above
            winners_match_list.remove(s+1)
            losers_match_list.append(winners_match_list[s])
            winners_match_list.remove(winners_match_list[s])
        rem_match_count -= 1
        s += 1

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))

    # losers until GF
    s = 0
    while len(losers_match_list) > 1:
        print("Losers' round")
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[s]) + " vs " + str(losers_match_list[s+1]) + ": "))
        if new_winner == 1:
            losers_match_list.remove(losers_match_list[s+1])
            losers_match_list.append(s) # put winners at end again so order isn't disrupted - rebuilds list
            losers_match_list.remove(s) # remove winner from start so not cycled over
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        elif new_winner == 2:
            losers_match_list.append(s+1) # see above
            losers_match_list.remove(s+1)
            losers_match_list.remove(winners_match_list[s])
        rem_match_count -= 1
        s += 1

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))

"""

s = 0
e = len(winners_match_list)
while rem_match_count != 0:
    # first round
    while e != player_count / 2:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(n[0])
            winners_match_list.append(n[1])
        elif new_winner == 1:
            losers_match_list.append(n[1])
            winners_match_list.append(n[0])
        rem_match_count -= 1 # reduce match count after declaration of winner

    print("init round winners: " + str(winners_match_list))
    print("init round losers:  " + str(losers_match_list))

    # losers play each other
    s = 0
    e = len(losers_match_list) / 2

    while s != e:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
        elif new_winner == 1:
            losers_match_list.append(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
        rem_match_count -= 1
        s += 1

    print("DEBUG: losers_match_list = " + str(losers_match_list))

    # winners play each other - goes bad with more than 8 players
    s = 0
    e = len(winners_match_list) / 2

    while s != e:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
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
        rem_match_count -= 1
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
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
        elif new_winner == 1:
            losers_match_list.append(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
        rem_match_count -= 1
        s += 1

    print("DEBUG: losers_match_list = " + str(losers_match_list))

    # winners again
    s = 0
    e = len(winners_match_list) / 2

    while s != e:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
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
        rem_match_count -= 1
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
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
        elif new_winner == 1:
            losers_match_list.append(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
        rem_match_count -= 1
        s += 1
    print("DEBUG: losers_match_list = " + str(losers_match_list))

    if len(losers_match_list) == len(losers_waiting):
        losers_match_list.append(losers_waiting[-1])
        losers_waiting.remove(losers_waiting[-1])

    # losers final
    s = 0
    e = len(losers_match_list) / 2

    while s != e:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[0]) + " vs " + str(losers_match_list[1]) + ": "))
        if new_winner == 2:
            losers_match_list.append(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
        elif new_winner == 1:
            losers_match_list.append(losers_match_list[0])
            losers_match_list.remove(losers_match_list[1])
            losers_match_list.remove(losers_match_list[0])
        rem_match_count -= 1
        s += 1
    print("DEBUG: losers_match_list = " + str(losers_match_list))

    if len(losers_match_list) == 1 and len(losers_waiting) == 0:
        winners_match_list.append(losers_match_list[0])

    # grand final
    s = 0
    e = len(winners_match_list) / 2

    while s != e:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(winners_match_list[1]) + ": "))
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
        rem_match_count -= 1
        s += 1

    print("DEBUG: winners_match_list = " + str(winners_match_list))
    print("DEBUG: losers_match_list = " + str(losers_match_list))

    # if rem_match_count == 0:
    if len(winners_match_list) == 1:
        print("The winner is " + str(winners_match_list[0]) +"!")
    """
    print("END")
