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
losers_match_list = []

# for debug, delete later
winners_match_list = [["John", "Joe"], ["Todd", "Tess"], ["Karen", "Katarina"], ["Elizabeth", "Edward"]]

while match_count > 0:
    while len(winners_match_list[0]) > 1:
    # need to change winners_match_list to be a list of paired players rather than just a list of players
        new_losers_match = []
        for n in winners_match_list:
            new_winner = int(input("Please enter winner of " + str(n) + " (1/2): 1) " + str(n[0]) + " or 2) " + str(n[1]) + " "))
            if new_winner == 2:
                new_losers_match.append(n[0])
                n.remove(n[0])
            elif new_winner == 1:
                new_losers_match.append(n[1])
                n.remove(n[1])
            else:
                print("Invalid entry.")
                break
            if len(new_losers_match) % 2 == 0 and len(new_losers_match) != 0:
                losers_match_list.append(new_losers_match)
                new_losers_match = []
            match_count -= 1
        if len(winners_match_list[0]) == 1 and len(winners_match_list) == 1:
            print(str((winners_match_list[0])[0]) + " reaches GF! Now to face off against the winner of the losers' bracket!")
        # format of winners_match_list is changed below at present
        elif len(winners_match_list[0]) == 1 and len(winners_match_list) != 1:
            while len(winners_match_list[0]) != 2:
                # inconsistent pruning of winners list (individuals are left as lists until this step, potentially can be improved)
                winners_match_list.append([(winners_match_list[0])[0], (winners_match_list[1])[0]])
                winners_match_list.remove(winners_match_list[1])
                winners_match_list.remove(winners_match_list[0])
        else:
            print("ERROR!")
        # losers match inputs
    while len(losers_match_list[0]) > 1:
        for n in losers_match_list:
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
        elif len(losers_match_list[0]) == 1 and len(losers_match_list) != 1:
            while len(losers_match_list[0]) != 2:
                # inconsistent pruning of winners list (individuals are left as lists until this step, potentially can be improved)
                losers_match_list.append([(losers_match_list[0])[0], (losers_match_list[1])[0]])
                losers_match_list.remove(losers_match_list[1])
                losers_match_list.remove(losers_match_list[0])
        else:
                print("ERROR!")
print("END")
