# import datetime
# import requests
# from player import Player

from playerreader import PlayerReader
from playerstats import PlayerStats

def main():

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url).get_players()
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

#    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
#    response = requests.get(url).json()
#    players = []
#    for player_dict in response:
#        if player_dict['nationality']=='FIN':
#            player = Player(
#                player_dict['name'],
#                player_dict['nationality'],
#                player_dict['assists'],
#                player_dict['goals'],
#                player_dict['penalties'],
#                player_dict['team'],
#                player_dict['goals']
#            )
#            players.append(player)
#            players.append(str(player))
#    print("Players from FIN " + str(datetime.datetime.now()) + "\n")
#    players = sorted(players, key=lambda x: int(x.split("=")[1]), reverse=True)
#    for player in players:
#        print(player)

if __name__ == "__main__":
    main()
