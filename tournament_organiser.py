# simple tournament organiser (only double elim, single pool at the moment, only 8 players tested atm)

player_count = -1
while player_count < 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
    except ValueError:
        continue

# for debugging
# player_count = 16

init_match_list = []

# currently seed position is stored in order in the list, no key-value pair
for n in range(player_count):
    init_match_list.append(input("Please enter seed %d name: " % (n + 1)))

# for debugging - now testing 16 players
# init_match_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# needs better formatting
print("Players: " + str(init_match_list))

# formula for double elim
init_match_count = (player_count - 1) * 2 + 1
rem_match_count = init_match_count
# establish lists for use below
losers_match_list = []
winners_match_list = []

# reserved section for matches in case of uneven number of players
if player_count % 2 != 0:
    uneven = True
    print("Preliminary round")
    # lowest seeds play each other
    while True:
        try:
            new_winner = int(input("Please enter 1 or 2 to select winner of " + str(init_match_list[-1]) + " vs " + str(init_match_list[-2]) + ": "))
        except ValueError:
            print("Please enter 1 or 2")
        else:
            if new_winner != 1 and new_winner != 2:
                print("Please enter 1 or 2")
                continue
            else:
                break
    if new_winner == 1:
        # declare loser
        uneven_loser = init_match_list[-2]
        # remove loser from init_match_list
        init_match_list.remove(init_match_list[-2])
    elif new_winner == 2:
        # declare loser
        uneven_loser = init_match_list[-1]
        # remove loser from init_match_list
        init_match_list.remove(init_match_list[-1])
    rem_match_count -= 1
else:
    uneven = False

# init matches - matches 1st seed vs 8th seed etc, not sure if this is the preferred method
print("Initial round")
s = 0
e = len(init_match_list) - 1
while s != e + 1: # breaks when the while loop reaches the middle of the list
    while True:
        try:
            new_winner = int(input("Please enter 1 or 2 to select winner of " + str(init_match_list[s]) + " vs " + str(init_match_list[e]) + ": "))
        except ValueError:
            print("Please enter 1 or 2")
        else:
            if new_winner != 1 and new_winner != 2:
                print("Please enter 1 or 2")
                continue
            else:
                break
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

# uneven losers match
if uneven == True:
    print("Additional losers' round")
    while True:
        try:
            new_winner = int(input("Please enter 1 or 2 to select winner of " + str(uneven_loser) + " vs " + str(losers_match_list[-1]) + ": "))
        except ValueError:
            print("Please enter 1 or 2")
        else:
            if new_winner != 1 and new_winner != 2:
                print("Please enter 1 or 2")
                continue
            else:
                break
    if new_winner == 1:
        # declare uneven winner
        uneven_winner = uneven_loser
        # remove loser from losers_match_list
        losers_match_list.remove(losers_match_list[-1])
        # add uneven_winner to losers_match_list in their place
        losers_match_list.append(uneven_winner)
    elif new_winner == 2:
        # no need to do anything just leave losers_match_list in place
        uneven_loser = []
        uneven_winner = []
    rem_match_count -= 1
    uneven = False

# winners and losers repeating matches
while rem_match_count > 2:
    # losers until GF
    s = 0
    keep_in_losers = []
    eliminated = []
    while len(losers_match_list) > (len(keep_in_losers) * 2) or len(losers_match_list) % 2 != 0:
        print("Losers' round")
        while True:
            try:
                new_winner = int(input("Please enter 1 or 2 to select winner of " + str(losers_match_list[s]) + " vs " + str(losers_match_list[s+1]) + ": "))
            except ValueError:
                print("Please enter 1 or 2")
            else:
                if new_winner != 1 and new_winner != 2:
                    print("Please enter 1 or 2")
                    continue
                else:
                    break
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
    # added condition that winners_match_list is greater than losers_match_list
    # otherwise larger player counts losers get inserted incorrectly into losers_match_list
    # must be an exception for when both lists have length 2, however
    if len(winners_match_list) != 1 and (len(winners_match_list) > len(losers_match_list) or len(winners_match_list) == 2):
        keep_in_winners = []
        while len(winners_match_list) > (len(keep_in_winners) * 2) or len(winners_match_list) % 2 != 0:
            print("Winners' round")
            while True:
                try:
                    new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[s]) + " vs " + str(winners_match_list[s+1]) + ": "))
                except ValueError:
                    print("Please enter 1 or 2")
                else:
                    if new_winner != 1 and new_winner != 2:
                        print("Please enter 1 or 2")
                        continue
                    else:
                        break
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
while True:
    try:
        new_winner = int(input("Please enter 1 or 2 to select winner of " + str(winners_match_list[0]) + " vs " + str(losers_match_list[0]) + ": "))
    except ValueError:
        print("Please enter 1 or 2")
    else:
        if new_winner != 1 and new_winner != 2:
            print("Please enter 1 or 2")
            continue
        else:
            break
# declare winner
if new_winner == 1:
    print(str(winners_match_list[0]) + " is the winner!")
elif new_winner == 2:
    print(str(losers_match_list[0]) + " is the winner!")
rem_match_count -= 1

print("END")
