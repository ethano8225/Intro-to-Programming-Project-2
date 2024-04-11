####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34260003

""" Implement the main program and functions below """
from Player import Player 

def display_menu():
    """display_menu() displays the main menu to the user."""

    print("1-List all players")
    print("2-List all players with at least a specific number of goals")
    print("3-List all players in a specific league")
    print("4-Find a specific player")
    print("5-Determine the player with the most goals")
    print("6-Determine total points for all players and print out the values")
    print("7-Exit\n")

def initialize():
    """initialize() creates the given player list, and returns the list."""

    P1 = Player("Erling Haaland",     "EPL",          18,  5,  270)
    P2 = Player("Robert Lewandowski", "La Liga",      12,  6,  414)
    P3 = Player("Harry Kane",         "Bundesliga",   30,  6,  472)
    P4 = Player("Son Heung-Min",      "EPL",          14,  8,  660)
    P5 = Player("Julian Alvarez",     "EPL",           8,  8,  915)
    P6 = Player("Leroy Sane",         "Bundesliga",    8, 11,  903)
    P7 = Player("Mohamed Salah",      "EPL",          15,  9,  686)
    P8 = Player("Jude Bellingham",    "La Liga",      16,  3, 1164)
    P9 = Player("Toni Kroos",         "La Liga",       1,  7, 1908)
    P10= Player("Sehrou Guirassy",    "Bundesliga",   21,  1,  494)
    playerList= [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]
    return playerList

def required_line():        
    """Prints the Name, League,...,Passes above the players' information."""
    
    print(f"{"Name":20}{"League":>10}{"Goals":>10}{"Assists":>10}{"Passes":>10}")

def display_goal(minGoals):
    """display_goal() displays the players that have more than x goals (x being the user input)."""
    minGoals = int(minGoals)
    if minGoals >= 0:
        for playerX in playerList:
            if  playerX.goals >= minGoals:          # only print if player goals is greater than user input
                playerX.print_player()
            elif minGoals > 30:                     # no player has more than 30 goals, print if 
                print("No players found.")          # user input > 30
    else:
        print("Invalid (text or negative number) input.")


def display_league(leagueName):
    """display_league() shows players that are in a user-selected league."""
    
    if len(leagueName) == 3:                        # if input is length of EPL, uppercase
        leagueName = leagueName.upper()             # in case "epl" was typed (or sth similar)
    if len(leagueName) == 10:                       
        leagueName = leagueName.title()             # same idea here for Bundesliga and La Liga
    if len(leagueName) == 7 and len(leagueName.split()) == 2:
        name = leagueName.split()
        la = (name[0]).title()                      # la liga requires more code to uppercase
        liga = (name[1]).title()                    # due to title only capatalizing first letter
        leagueName = la + " " + liga

    if leagueName != "EPL" and leagueName != "Bundesliga" and leagueName != "La Liga":
        print("No players found.")
        return 0
    else:
        required_line()                          # only print for valid leagues

    for playerX in playerList:                  # displays players with specific league,                  
        if playerX.league == leagueName:        # if leagueName is not a league in the set, 
            playerX.print_player()              # return no players found.


def display_player(user_input):
    """display_player() shows information for a user-selected player."""
    a=0
    for playerX in playerList:
        a=a+1
        if playerX.name == user_input:         # for loop to go through all the players
            playerX.print_player()             # and check if the name matches.
            a=a-1                              # also keeps track if no players were printed
        elif a==10:
            print("No players found.")


def display_most_goals():
    """display_most_goals() shows the player with the most goals, along with how many goals they have."""
    mostGoals=0
    for player in range(len(playerList)):       # for loop to go through players.
        playerX = playerList[player]
        if playerX.goals > mostGoals:           # Set mostGoals to a higher value if that player
            mostGoals=playerX.goals             # has more goals. also keep track of the spot 
            topGoalScorer = player              # in the list where the top goal scorer is
    topPlayer = playerList[topGoalScorer]
    print(f"{topPlayer.name} has the most goals with {topPlayer.goals}.\n")


def calculate_total_points():
    """calculate_total_points() displays the total points for each player in your fantasy league."""
    for playerX in playerList:                              # goals = 2.5 pts per, assists is .93 per, passes are .05 per.
        total_points = round(float(playerX.goals)*2.5+float(playerX.assists)*.93+float(playerX.passes)*.05,2)
        print(f"{playerX.name} has {total_points} points.") # print out the player with x amount of fantasy points.
    print("")                                               # provide a newline for the new menu prompt



print("Welcome to your Fantasy Team Database!")
print("====================\n")
playerList = initialize()

while True:
    display_menu()
    option=input("Enter Command: ")
    

    if option =="1":
        required_line()
        for playerX in playerList:      # easy way to list all players
            playerX.print_player()
        print("")                       # provide a newline for the new menu prompt
        

    if option =="2":
        while True:
            min_goals=input("Please indicate number of goals: ")
            if min_goals.isdecimal() == True:           # if isdecimal() returns true, print the players,             
                break                                   # if not, say invalid input, and don't break 
            elif min_goals.isnumeric() == False:        # so it asks the user again
                print("Invalid (negative or text) input.\n")      
                
        if int(min_goals) >= 0 and int(min_goals) < 31:
            required_line()                             # print the line if user input is in the valid range
        display_goal(min_goals)
        print("")              


    if option =="3":
        while True:
            selected_league=input("Please indicate the league: ")  
            if selected_league.isdecimal() == True:            
                print("Invalid (number) input.\n")  
            if selected_league.isdecimal() == False:           # if isdecimal() returns false, print the players 
                display_league(selected_league)                # if its true, re-ask for input
                print("") 
                break                                          # provide a newline for the new menu prompt    



    if option =="4":
        while True:
            selected_player=input("Please indicate name of player: ")  # check if user input is a number, if it
            if selected_player.isdecimal() == True:                    # is, display invalid input and ask again.
                print("Invalid (number) input.\n")
            elif selected_player.isdecimal() == False:
                break
        for playerX in playerList:                  # check if name exists, if it does, print out name/league...
            if playerX.name == selected_player:
                required_line()                     # only print if the player name is in the list
        display_player(selected_player)
        print("")                                   # provide a newline for the new menu prompt


    if option =="5":
        display_most_goals()
    
    if option =="6":
        calculate_total_points()

    if option =="7":
        print("Exiting")  # if they want to exit, break
        break