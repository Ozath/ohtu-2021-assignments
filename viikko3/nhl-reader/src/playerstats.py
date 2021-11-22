import datetime
from playerreader import PlayerReader

class PlayerStats:

    def __init__(self,reader):
        self.players = reader

    def top_scorers_by_nationality(self,nationality):
        players = []
        for player_id in self.players:
            if player_id.nationality=="FIN":
                players.append(f"{player_id.name:20} {player_id.team:3} {player_id.goals:>2} + {player_id.assists:>2} = {player_id.total:>2}")
        players = sorted(players, key=lambda x: int(x.split("=")[1]), reverse=True)
        a = "Players from FIN " + str(datetime.datetime.now()) + "\n"
        players.insert(0,a)
        return players
