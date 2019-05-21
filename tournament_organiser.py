# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested atm)
# for debugging
player_count = 8
"""
player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue
"""
# for debugging
init_match_list = [1, 2, 3, 4, 5, 6, 7, 8]
"""
init_match_list = []

# currently seed position is stored in order in the list, no key-value pair
for n in range(player_count):
    init_match_list.append(input("Please enter seed %d name: " % (n + 1)))
"""
# needs better formatting
print("Players: " + str(init_match_list))

# formula for double elim
init_match_count = (player_count - 1) * 2 + 1
rem_match_count = init_match_count
# establish lists for use below
losers_match_list = []
winners_match_list = []

# reserved section for matches in case of uneven number of players

# init matches - matches 1st seed vs 8th seed etc, not sure if this is the preferred method
print("Initial round")
s = 0
e = len(init_match_list) - 1
while s != e + 1: # breaks when the while loop reaches the middle of the list
    new_winner = int(input("Please enter 1 or 2 to select winner of " + str(init_match_list[s]) + " vs " + str(init_match_list[e]) + ": "))
    if new_winner == 1:
        # adds winner to winners
        winners_match_list.append(init_match_list[s])
        # adds loser to losers
        losers_match_list.append(init_match_list[e])
    elif new_winner == 2:
        # adds winner to winners
        winners_match_list.append(init_match_list[e])
        # adds loser to losers
        losers_match_list.append(init_match_list[s])
    rem_match_count -= 1
    s += 1
    e -= 1

print("Winners: " + str(winners_match_list))
print("Losers: " + str(losers_match_list))

# winners and losers repeating matches
while rem_match_count > 1:
    # winners until GF
    s = 0
    while len(winners_match_list) > 1: # need to fix these so repeats happen properly
        print("Winners' round")
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[s]) + " vs " + str(winners_match_list[s+1]) + ": "))
        if new_winner == 1:
            # add loser to losers
            losers_match_list.append(winners_match_list[s+1])
            # remove loser from winners
            winners_match_list.remove(winners_match_list[s+1])
            # append winner to end of winners to rebuild list
            winners_match_list.append(winners_match_list[s])
            # remove winner from beginning of winners so cycles correctly
            winners_match_list.remove(winners_match_list[s])
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        elif new_winner == 2:
            # append winner to end of winners to rebuild list
            winners_match_list.append(winners_match_list[s+1])
            # remove winner from beginning of winners so cycles correctly
            winners_match_list.remove(winners_match_list[s+1])
            # add loser to losers
            losers_match_list.append(winners_match_list[s])
            # remove loser from winners
            winners_match_list.remove(winners_match_list[s])
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        rem_match_count -= 1
        s += 1

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))

    # losers until GF
    s = 0
    while len(losers_match_list) > 1: # need to fix these so repeats happen properly
        print("Losers' round")
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[s]) + " vs " + str(losers_match_list[s+1]) + ": "))
        if new_winner == 1:
            # remove loser from losers (eliminated)
            losers_match_list.remove(losers_match_list[s+1])
            # append winner to end of losers to rebuild list (continues in losers)
            losers_match_list.append(losers_match_list[s])
            # remove winner from beginning of losers so cycles correctly
            losers_match_list.remove(losers_match_list[s])
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        elif new_winner == 2:
            # append winner to end of losers to rebuild list (continues in losers)
            losers_match_list.append(losers_match_list[s+1])
            # remove winner from beginning of winners so cycles correctly
            losers_match_list.remove(losers_match_list[s+1])
            # remove loser from losers (eliminated)
            losers_match_list.remove(losers_match_list[s])
            # this order is necessary - s+1 must be removed before s, as the removal of s will change which index s+1 is
        rem_match_count -= 1
        s += 1

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))
print("END")
