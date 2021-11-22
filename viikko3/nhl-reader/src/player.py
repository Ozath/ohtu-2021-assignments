class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = str(assists)
        self.goals = str(goals)
        self.penalties = str(penalties)
        self.team = team
        self.games = str(games)
        self.total = str(goals + assists)
    
    def __str__(self):
#        return str(self.name + " team " + self.team + "  goals " + self.goals + " assists " + self.assists)
        return f"{self.name:20} {self.team:3} {self.goals:>2} + {self.assists:>2} = {self.total:>2}"
