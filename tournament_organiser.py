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
initial_match_list = []
initial_matches_count = round(player_count / 2)
# iterates through players without for loop
s = 0
e = player_count - 1
for n in range(initial_matches_count):
    # currently matches 1 vs last and goes inward, is this ideal?
    initial_match_list.append([player_names[int(s)], player_names[int(e-s)]])
    s += 1

# needs better formatting
print("Initial matches: " + str(initial_match_list))

# establish lists for use below
winners_match_list = initial_match_list
losers_match_list = []

# winners' matches inputs
while len(winners_match_list[0]) > 1: # while the first list of winners_match_list has more than 1 player
    new_losers_match = [] # temporary pairing for losers to go in losers_match_list
    for n in winners_match_list:
        # for each pairing in winners_match_list, the for loop asks for the victor
        new_winner = int(input("Please enter winner of " + str(n) + " (1/2): 1) " + str(n[0]) + " or 2) " + str(n[1]) + " "))
        # removes loser from winners_match_list into new_losers_match (temporary pairing storage)
        if new_winner == 2:
            new_losers_match.append(n[0])
            n.remove(n[0])
        elif new_winner == 1:
            new_losers_match.append(n[1])
            n.remove(n[1])
        # haven't tested the else
        else:
            print("Invalid entry.")
            break
        # when temporary storage becomes at least 2, moves to new_losers_match and clears
        if len(new_losers_match) % 2 == 0 and len(new_losers_match) != 0:
            losers_match_list.append(new_losers_match)
            new_losers_match = []
        match_count -= 1
    # after iterating through winners matches, sees if 1 person left and puts them into grand final
    if len(winners_match_list[0]) == 1 and len(winners_match_list) == 1:
        print(str((winners_match_list[0])[0]) + " reaches GF! Now to face off against the winner of the losers' bracket!")
    # otherwise cleans up winners match list below. invidivuals are left as lists until below, not ideal
    elif len(winners_match_list[0]) == 1 and len(winners_match_list) != 1:
        while len(winners_match_list[0]) != 2:
            winners_match_list.append([(winners_match_list[0])[0], (winners_match_list[1])[0]])
            winners_match_list.remove(winners_match_list[1])
            winners_match_list.remove(winners_match_list[0])
    # not tested
    else:
        print("ERROR!")

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
