import csv


# open file and return ordered dictionaries of players
def import_players(file, new_line, delimiter):
    with open(file, newline=new_line) as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=delimiter)
        players = list(file_reader)

        return players


def sort_players(players):
    # list to hold experienced players
    inexperienced = []
    # list to hold inexperienced players
    experienced = []
    # loop through players
    for player in players:
        # place in appropriate group
        if player['Soccer Experience'] == "NO":
            inexperienced.append(player)
        else:
            experienced.append(player)
    # return groups
    return inexperienced, experienced


def assign_players(players, teams):
    index = 0
    # sort players into experienced and un-experienced
    # returns 2 groups, inexperienced and experienced
    sorted_players = sort_players(players)
    # list of players to return to the script
    player_list = []
    # loop through the group
    for group in sorted_players:
        # set range = to the number of teams, use this
        # value to select a team based on its current index
        range = len(teams) - 1
        # loop through players in this group
        for player in group:
            # assign player to the current team (index value)
            player['Team'] = teams[index]
            # add the updated player to a clean list
            player_list.append(player)
            # if index is less than the number of teams,
            if index < range:
                # increment by one..
                index += 1
            else:
                # otherwise reset the index
                index = 0
    # return an updated list of players with their team assignments
    return player_list


if __name__ == "__main__":
    # open file & get players
    imported_players = import_players('soccer_players.csv', '', ',')

    # list of team names
    team_names = [
        "Sharks",
        "Dragons",
        "Raptors"
    ]

    player_list = assign_players(imported_players, team_names)

    for player in player_list:
        print(player['Name'], player['Team'], player['Soccer Experience'])


# save to teams
# output file
