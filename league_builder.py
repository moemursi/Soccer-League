import csv


# open file and return ordered dictionaries of players
def import_players(file, new_line, delimiter):
    with open(file, newline=new_line) as csvfile:
        file_reader = csv.DictReader(csvfile, delimiter=delimiter)
        players = list(file_reader)

        return players


# put logic here
if __name__ == "__main__":
    # open file & get players
    players = import_players('soccer_players.csv', '', ',')

    # setup teams
    teams = {
        "Sharks",
        "Dragons",
        "Raptors"
    }

    # sort players
    inexperienced_players = []
    experienced_players = []

    # sort into groups of experienced & un experienced
    for player in players:
        print(player['Name'], player['Soccer Experience'])

        if player['Soccer Experience'] == "NO":
            inexperienced_players.append(player)
        else:
            experienced_players.append(player)

    for player in inexperienced_players:
        print(player['Name'], player['Soccer Experience'])

    for player in experienced_players:
        print(player['Name'], player['Soccer Experience'])


# save to teams
# output file
