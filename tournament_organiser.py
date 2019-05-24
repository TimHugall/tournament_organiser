# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested atm)
# for debugging
# player_count = 8

player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue

# for debugging
# init_match_list = [1, 2, 3, 4, 5, 6, 7, 8]

init_match_list = []

# currently seed position is stored in order in the list, no key-value pair
for n in range(player_count):
    init_match_list.append(input("Please enter seed %d name: " % (n + 1)))

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
while rem_match_count > 2:
    # losers until GF
    s = 0
    keep_in_losers = []
    eliminated = []
    while len(losers_match_list) > (len(keep_in_losers) * 2) or len(losers_match_list) % 2 != 0:
        print("Losers' round")
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[s]) + " vs " + str(losers_match_list[s+1]) + ": "))
        if new_winner == 1:
            # add loser to eliminated
            eliminated.append(losers_match_list[s+1])
            # add winner to keep_in_losers
            keep_in_losers.append(losers_match_list[s])
        elif new_winner == 2:
            # add loser to eliminated
            eliminated.append(losers_match_list[s])
            # add winner to keep_in_losers
            keep_in_losers.append(losers_match_list[s+1])
        rem_match_count -= 1
        # needed otherwise s is too high near end
        if len(losers_match_list) > 3:
            s += 2
        else:
            break

    # so that losers final qualification works
    if len(losers_match_list) == 3:
        keep_in_losers.append(losers_match_list[-1])
    losers_match_list = keep_in_losers

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))

    # winners until GF
    s = 0
    move_to_losers = []
    if len(winners_match_list) != 1:
        keep_in_winners = []
        while len(winners_match_list) > (len(keep_in_winners) * 2) or len(winners_match_list) % 2 != 0:
            print("Winners' round")
            new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[s]) + " vs " + str(winners_match_list[s+1]) + ": "))
            if new_winner == 1:
                # add loser to move_to_losers
                move_to_losers.append(winners_match_list[s+1])
                # add winner to keep_in_winners
                keep_in_winners.append(winners_match_list[s])
            elif new_winner == 2:
                # add loser to move_to_losers
                move_to_losers.append(winners_match_list[s])
                # add winner to keep_in_winners
                keep_in_winners.append(winners_match_list[s+1])
            rem_match_count -= 1
            s += 2
        winners_match_list = keep_in_winners

        # move to losers here
        if len(move_to_losers) == 1: # ensures that winners' final loser is placed properly
            losers_match_list.append(move_to_losers[0])
        else:
            s = 1
            for n in move_to_losers:
                losers_match_list.insert(s, n)
                s += 2

    print("Winners: " + str(winners_match_list))
    print("Losers: " + str(losers_match_list))

# grand final
print("Grand final")
new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(losers_match_list[0]) + ": "))
# declare winner
if new_winner == 1:
    print(str(winners_match_list[0]) + " is the winner!")
elif new_winner == 2:
    print(str(losers_match_list[0]) + " is the winner!")
rem_match_count -= 1

print("END")
