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


def assign_players(players, team_list):
    index = 0
    # sort players into experienced and un-experienced
    # returns 2 groups, inexperienced and experienced
    sorted_players = sort_players(players)
    # list of players to return to the script
    player_list = []
    # list of teams
    teams = []
    # break team dictionary into a list
    for key, value in team_list.items():
        teams.append(key)
    # loop through the 2 player groups
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


def populate_teams(team_list, player_list):

    for player in player_list:
        team = player['Team']
        if team in team_list:
            team_list[team].append(player)

    return team_list


def write_teams(teams):
    file = open('teams.txt', 'a')
    for team, players in teams.items():
        file.write(team + "\n")
        for player in players:
            # set vars to the write line is easier to read
            name = player['Name']
            experience = player['Soccer Experience']
            guardians = player['Guardian Name(s)']
            file.write("{}, {}, {}\n".format(name, experience, guardians))
        file.write("\n")



if __name__ == "__main__":
    # open file & get players
    imported_players = import_players('soccer_players.csv', '', ',')

    # list of team names
    team_list = {
        'Sharks': [],
        'Dragons': [],
        'Raptors': []
    }

    # assign players to teams
    assigned_players = assign_players(imported_players, team_list)
    # populate team lists
    teams = populate_teams(team_list, assigned_players)

    # testing
    for team, players in teams.items():
        print("**" + team + "**")
        for player in players:
            print(player['Name'], player['Soccer Experience'])
        print("\n")

    # output file
    write_teams(teams)

