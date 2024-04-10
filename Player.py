####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34260003

""" Implement the Player class and functions below """

class Player:
    def __init__(self,name,league,goals,assists,passes):
        self.name = name
        self.league = league         # all players have these attributes
        self.goals = goals
        self.assists = assists
        self.passes = passes
    def print_player(self):          # simple one-line to display information of a player cleanly (for all players)
        print("{0:20}{1:>10}{2:10}{3:10}{4:10}".format(self.name,self.league,self.goals,self.assists,self.passes))