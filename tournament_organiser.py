# simple tournament organiser
# module imports
import numpy as np
import pandas as pd
import json

# player count
player_count = -1
while player_count < 1 or player_count == 1:
    try:
        player_count = int(input("How many players will be participating in the tournament? "))
        continue
    except ValueError:
        continue

standing = player_count

# prompt to import
while True:
    import_seeds = input( "Do you wish to assign some seedings from a previous standings.json file? (y/n) ")
    if import_seeds.lower() != "y" and import_seeds.lower() != "n":
        print("Invalid input.")
        continue
    else:
        break
print(" ")

# define function to search lists of dictionaries
# could implement binary search although sorting it in the first place is probably not worth it
def search_lod(key, value, list_of_dicts):
    cycle = 0
    for p in list_of_dicts:
        if p[key] == value:
            return p
        else:
            cycle += 1
            if cycle == len(list_of_dicts):
                return None
            else:
                continue

# if no imports, put players in a normal list
# the following 3 commented-out sections were replaced by the list comprehension
# init_match_list = []
if import_seeds == "n":
#    for n in range(player_count):
#        init_match_list.append(input("Please enter seed %d name: " % (n + 1)))
    init_match_list = [(input("Please enter seed %d name: " % (n + 1))) for n in range(player_count)]
# otherwise import some
else:
    with open('standings.json', 'r') as imported_standings:
        imported_standings = json.load(imported_standings)
    relevant_imported_standings = []
    new_players = []

    # check if some players are in imported standings
    for n in range(player_count):
        player_name = input("Please enter player name: ")
        find_name = search_lod('name', player_name, imported_standings)
        if find_name is not None:
            relevant_imported_standings.append(find_name)
            print("%s found in imported standings." % player_name)
            print(" ")
        else:
            new_players.append(player_name)
    print("Seeding returning players based on imported standings.")

    # add found players to init_match_list
    i = 1
    while i <= len(imported_standings):
        find_seed = search_lod('seed', i, relevant_imported_standings)
        if find_seed is not None:
            init_match_list.append(find_seed['name'])
        i += 1

    # seed remaining non-imports
    print("List of players not in imported standings: " + str(new_players))
    print(" ")
    new_seeds_list = []

    # determining valid seed values remaining
    valid_seed_inputs = []
    i = 0
    while len(valid_seed_inputs) + len(init_match_list) < player_count:
        valid_seed_inputs.append(player_count - i)
        i += 1

    # prompt for seeding for new players
    for n in new_players:
        while True:
            try:
                new_seed = int(input("What seed should " + str(n) + " be? Valid values: " + str(valid_seed_inputs) + " "))
                if new_seed in valid_seed_inputs:
                    new_seeds_list.append({'name': str(n), 'seed': new_seed})
                    valid_seed_inputs.remove(new_seed)
                    break
                else:
                    print("Invalid input.")
                    continue
            except ValueError:
                print("Invalid input.")
                continue
            if len(new_seeds_list) + len(init_match_list) == player_count:
                break

    # search list to assign order and append to init_match_list
    i = len(init_match_list) + 1
    while i <= player_count:
        find_seed = search_lod('seed', i, new_seeds_list)
        init_match_list.append(find_seed['name'])
        i += 1
    print(" ")
    print("List of players in seeded order: " + str(init_match_list))

# stats
stats = []
for player in init_match_list:
    player_stats = {}
    player_stats["standing"] = 0
    player_stats["name"] = player
    player_stats["seed"] = (int(init_match_list.index(player)) + 1)
    player_stats["wins"] = 0
    player_stats["losses"] = 0
    stats.append(player_stats)

# could format better
print(" ")
print("Players: " + str(init_match_list))

# formula for double elim
rem_match_count = (player_count - 1) * 2 + 1

# establish lists, variables for use below
losers_match_list = []
winners_match_list = []
winner = ""
loser = ""

# define function to ask user for match result
def resultQuery(player_one, player_two):
    global winner, loser, rem_match_count, stats, standing
    while True:
        try:
            selection = 0
            while selection != 1 and selection != 2:
                selection = int(input("Please enter 1 or 2 to select the winner of " + str(player_one) + " vs " + str(player_two) + ": "))
            if selection == 1:
                winner = player_one
                loser = player_two
            elif selection == 2:
                winner = player_two
                loser = player_one
            # modify player stats
            # go through list with next, use item, for each item in list 'stats', if item matches criteria, set dict entry to be that item
            # doesn't need a fallback if player isn't found in list as player should always be found
            dict_winner = next(item for item in stats if item["name"] == winner)
            # increase win count
            dict_winner['wins'] += 1
            # standing - give 1st place if on the last match and won
            if standing == 2:
                dict_winner['standing'] = 1
            # see above
            dict_loser = next(item for item in stats if item["name"] == loser)
            # increase loss count
            dict_loser['losses'] += 1
            # set standing based on how close to end (may need tweaking for equal 5th place etc.)
            # gives 2nd place if lost grand final
            if standing == 2:
                dict_loser['standing'] = 2
            elif dict_loser['losses'] == 2:
                dict_loser['standing'] = standing
                standing -= 1
            rem_match_count -= 1
            return rem_match_count, winner, loser, stats
        except ValueError:
            print("Invalid input.")
        else:
            if selection != 1 and selection != 2:
                print("Invalid input.")
                continue
            else:
                break

# define function to print brackets
def print_brackets(winners_match_list, losers_match_list):
    print(" ")
    print("Winners' bracket: " + str(winners_match_list))
    print("Losers' bracket: " + str(losers_match_list))

# reserved section for matches in case of uneven number of players
if player_count % 2 != 0:
    uneven = True
    print(" ")
    print("Preliminary round (due to uneven players)")
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
while s != e + 1:  # breaks when the while loop reaches the middle of the list
    resultQuery(init_match_list[s], init_match_list[e])
    # adds winner to winners
    winners_match_list.append(winner)
    # adds loser to losers
    losers_match_list.append(loser)
    s += 1
    e -= 1

# uneven losers match
if uneven == True:
    print(" ")
    print("Additional losers' round")
    losers_match_list.append(uneven_loser)
    resultQuery(losers_match_list[-1], losers_match_list[-2])
    # remove loser from losers_match_list, winner stays
    losers_match_list.remove(loser)
    uneven = False

print_brackets(winners_match_list, losers_match_list)

# winners and losers repeating matches
while rem_match_count > 2:
    # losers until GF
    s = 0
    keep_in_losers = []
    eliminated = []
    while len(losers_match_list) > (len(keep_in_losers) * 2) or len(losers_match_list) % 2 != 0:
        print(" ")
        print("Losers' round")
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

    print_brackets(winners_match_list, losers_match_list)

    # winners until GF
    s = 0
    move_to_losers = []
    # added condition that winners_match_list is greater than losers_match_list
    # otherwise larger player counts losers get inserted incorrectly into losers_match_list
    # must be an exception for when both lists have length 2, however
    if len(winners_match_list) != 1 and (len(winners_match_list) > len(losers_match_list) or len(winners_match_list) == 2):
        print(" ")
        print("Winners' round")
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
        if len(move_to_losers) == 1:  # ensures that winners' final loser is placed properly
            losers_match_list.append(move_to_losers[0])
        else:
            s = 1
            for n in move_to_losers:
                losers_match_list.insert(s, n)
                s += 2

        print_brackets(winners_match_list, losers_match_list)

# grand final
print(" ")
print("Grand final")
resultQuery(winners_match_list[0], losers_match_list[0])
# declare winner
print(" ")
print(str(winner) + " is the winner!")
print(" ")
print("Results: ")
# prints standings at end
standings_list = sorted(stats, key=lambda k: k['standing']) # python lambda function. key is passed as 2nd parameter to sorted(),
# which is a function itself, taking argument k (key in dict) and returning value for 'standing' in that key in dict.
standings_df = pd.DataFrame(standings_list)
# print results without index, columns ordered correctly
print(standings_df[['standing', 'name', 'wins', 'losses', 'seed']].to_string(index=False))

with open('standings.json', 'w') as json_output:
    json.dump(standings_list, json_output)
