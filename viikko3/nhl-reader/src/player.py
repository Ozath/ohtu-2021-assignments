class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = str(assists)
        self.goals = str(goals)
        self.penalties = str(penalties)
        self.team = team
        self.games = str(games)
    
    def __str__(self):
        return self.name + " team " + self.team + "  goals " + self.goals + " assists " + self.assists
