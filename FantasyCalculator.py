####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34260003

""" Implement the main program and functions below """
import Player


P1 = Player.Player("Erling Haaland",     "EPL",          18, 5,  270)
P2 = Player.Player("Robert Lewandowski", "La Liga",      12, 6,  414)
P3 = Player.Player("Harry Kane",         "Bundesliga",   30, 6,  472)
P4 = Player.Player("Son Heung-Min",      "EPL",          14, 8,  660)
P5 = Player.Player("Julian Alvarez",     "EPL",          8,  8,  915)
P6 = Player.Player("Leroy Sane",         "Bundesliga",   8, 11,  903)
P7 = Player.Player("Mohamed Salah",      "EPL",          15, 9,  686)
P8 = Player.Player("Jude Bellingham",    "La Liga",      16, 3, 1164)
P9 = Player.Player("Toni Kroos",         "La Liga",      1,  7, 1908)
P10= Player.Player("Sehrou Guirassy",   "Bundesliga",    21, 1,  494)

playerList= [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]

def display_menu():
    print("1-List all players")
    print("2-List all players with at least a specific number of goals")
    print("3-List all players in a specific league")
    print("4-Find a specific player")
    print("5-Determine the player with the most goals")
    print("6-Determine total points for all players and print out the values")
    print("7-Exit\n")

print("Welcome to your Fantasy Team Database!")
print("====================\n\n")

def display_goal(user_input):
    for i in range(10):
        player_being_checked=playerList[i]
        if  player_being_checked.goals >= user_input:
            player_being_checked.listPlayers()
            print("")
        elif user_input>30:
            print("no players found")
            break
            
        
        
while True:
    display_menu()
    option=input("Enter Command: ")

    
    if option =="1":
        print("Name   \t\t\tLeague\t\tGoals\t\tAssists\t\tPasses")
        for i in playerList:
            i.listPlayers()
        print("")
        
    if option =="2":
        min_num_of_goals=int(input("minimum number of goals the player has scored"))
        display_goal(min_num_of_goals)

#        for i in range(9):
 #           player_being_checked=playerList[i]
  #          player_being_checked.listPlayers()
   #     print("")
                
"""
    if option =="3":

    
    if option =="4":

    
    if option =="5":

    
    if option =="6":
    

    if option =="7":
        print("Exiting")  #if they want to exit, break
        break
"""