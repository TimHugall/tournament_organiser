# simple tournament organiser
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

# stats
stats = []
for player in init_match_list:
    player_stats = {}
    player_stats["name"] = player
    player_stats["seed"] = (int(init_match_list.index(player)) + 1)
    player_stats["wins"] = 0
    player_stats["losses"] = 0
    stats.append(player_stats)

# for debugging - now testing 16 players
# init_match_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# needs better formatting
print("Players: " + str(init_match_list))

# formula for double elim
rem_match_count = (player_count - 1) * 2 + 1
# establish lists for use below
losers_match_list = []
winners_match_list = []

# function definitions
winner = ""
loser = ""
def resultQuery (player_one, player_two):
    global winner, loser, rem_match_count, stats
    while True:
        try:
            selection = int(input("Please enter 1 or 2 to select the winner of " + str(player_one) + " vs " + str(player_two) + ": "))
            if selection == 1:
                winner = player_one
                loser = player_two
            elif selection == 2:
                winner = player_two
                loser = player_one
            # needs section here to modify player stats
            # next(item for item in stats if item["name"] == winner) or something like this
            rem_match_count -= 1
            return rem_match_count
            return winner
            return loser
            return stats
        except ValueError:
            print("Invalid input.")
        else:
            if selection != 1 and selection != 2:
                print("Invalid input.")
                continue
            else:
                break

# reserved section for matches in case of uneven number of players
if player_count % 2 != 0:
    uneven = True
    print(" ")
    print("Preliminary round")
    # lowest seeds play each other
    resultQuery(init_match_list[-1], init_match_list[-2])
    # declare loser
    uneven_loser = loser
    # remove loser from init_match_list
    init_match_list.remove(loser)
else:
    uneven = False

# init matches - matches 1st seed vs 8th seed etc, not sure if this is the preferred method
print(" ")
print("Initial round")
s = 0
e = len(init_match_list) - 1
while s != e + 1: # breaks when the while loop reaches the middle of the list
    resultQuery(init_match_list[s], init_match_list[e])
    # adds winner to winners
    winners_match_list.append(winner)
    # adds loser to losers
    losers_match_list.append(loser)
    s += 1
    e -= 1

print("Winners' bracket: " + str(winners_match_list))
print("Losers' bracket: " + str(losers_match_list))

# uneven losers match
if uneven == True:
    print(" ")
    print("Additional losers' round")
    losers_match_list.append(uneven_loser)
    resultQuery(losers_match_list[-1], losers_match_list[-2])
    # remove loser from losers_match_list, winner stays
    losers_match_list.remove(loser)
    uneven = False

# winners and losers repeating matches
while rem_match_count > 2:
    # losers until GF
    print(" ")
    print("Losers' round")
    s = 0
    keep_in_losers = []
    eliminated = []
    while len(losers_match_list) > (len(keep_in_losers) * 2) or len(losers_match_list) % 2 != 0:
        resultQuery(losers_match_list[s], losers_match_list[s+1])
        # add loser to eliminated
        eliminated.append(loser)
        # add winner to keep_in_losers
        keep_in_losers.append(winner)
        # needed otherwise s is too high near end
        if len(losers_match_list) > 3:
            s += 2
        else:
            break

    # so that losers final qualification works
    if len(losers_match_list) == 3:
        keep_in_losers.append(losers_match_list[-1])
    losers_match_list = keep_in_losers

    print("Losers' bracket: " + str(losers_match_list))

    # winners until GF
    print(" ")
    print("Winners' round")
    s = 0
    move_to_losers = []
    # added condition that winners_match_list is greater than losers_match_list
    # otherwise larger player counts losers get inserted incorrectly into losers_match_list
    # must be an exception for when both lists have length 2, however
    if len(winners_match_list) != 1 and (len(winners_match_list) > len(losers_match_list) or len(winners_match_list) == 2):
        keep_in_winners = []
        while len(winners_match_list) > (len(keep_in_winners) * 2) or len(winners_match_list) % 2 != 0:
            resultQuery(winners_match_list[s], winners_match_list[s+1])
            # add loser to move_to_losers
            move_to_losers.append(loser)
            # add winner to keep_in_winners
            keep_in_winners.append(winner)
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

    print("Winners' bracket: " + str(winners_match_list))
    print("Losers' bracket: " + str(losers_match_list))

# grand final
print(" ")
print("Grand final")
resultQuery(winners_match_list[0], losers_match_list[0])
# declare winner
print(" ")
print(str(winner) + " is the winner!")
