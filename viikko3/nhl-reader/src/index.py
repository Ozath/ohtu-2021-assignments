import datetime
import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    players = []

    for player_dict in response:
        if player_dict['nationality']=='FIN':
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['goals']
            )
#            players.append(player)
            players.append(str(player))

    print("Players from FIN " + str(datetime.datetime.now()) + "\n")

    players = sorted(players, key=lambda x: int(x.split("=")[1]), reverse=True)

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
