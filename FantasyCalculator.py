####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34260003

""" Implement the main program and functions below """
import Player 

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

def initialize():
    P1 = Player.Player("Erling Haaland",     "EPL",          18,  5,  270)
    P2 = Player.Player("Robert Lewandowski", "La Liga",      12,  6,  414)
    P3 = Player.Player("Harry Kane",         "Bundesliga",   30,  6,  472)
    P4 = Player.Player("Son Heung-Min",      "EPL",          14,  8,  660)
    P5 = Player.Player("Julian Alvarez",     "EPL",           8,  8,  915)
    P6 = Player.Player("Leroy Sane",         "Bundesliga",    8, 11,  903)
    P7 = Player.Player("Mohamed Salah",      "EPL",          15,  9,  686)
    P8 = Player.Player("Jude Bellingham",    "La Liga",      16,  3, 1164)
    P9 = Player.Player("Toni Kroos",         "La Liga",       1,  7, 1908)
    P10= Player.Player("Sehrou Guirassy",    "Bundesliga",   21,  1,  494)
    playerList= [P1,P2,P3,P4,P5,P6,P7,P8,P9,P10]
    return playerList

def display_goal(user_input):
    for playerX in playerList:
        if  playerX.goals >= user_input:        # only print if player goals is greater than user input
            playerX.listPlayers()
        elif user_input > 30:                   # no player has more than 30 goals, print if 
            print("No players found.")          # user input > 30
            break
#add a check for invalid / negative input using else           
def display_league(user_input):
    count = 0
    for playerX in playerList:                  # displays players with specific league,
        count = count + 1                       # and checks to see if none are printed to say
        if playerX.league == user_input:        # no players found, if needed.
            count =  count - 1
            playerX.listPlayers()
        elif count == 10:
            print("No players found.")
            break
#change userinput to leaguename, change count for an if statement if input isnt epl, la liga or bundesliga, return 0
def display_player(user_input):
    a=0
    for playerX in playerList:
        a=a+1
        if playerX.name == user_input:         # for loop to go through all the players
            playerX.listPlayers()              # and check if the name matches.
            a=a-1                              # also keeps track if no players were printed
        elif a==10:
            print("No players found.")
        
def display_most_goals():
    mostGoals=0
    for i in range(10):                         # for loop to go through players.
        playerX = playerList[i]
        if playerX.goals > mostGoals:           # Set bestPlayerGoals to a higher value if that player
            mostGoals=playerX.goals             # has more goals.
            topGoalScorer = i
    topPlayer = playerList[topGoalScorer]
    print(f"{topPlayer.name} has the most goals with {topPlayer.goals}.\n")
    
def calculate_total_points():
    for playerX in playerList:                              # goals = 2.5 pts per, assists is .93 per, passes are .05 per.
        total_points = round(float(playerX.goals)*2.5+float(playerX.assists)*.93+float(playerX.passes)*.05,2)
        print(f"{playerX.name} has {total_points} points.") # print out the player with x amount of fantasy points.
    print("")                       # provide a newline for the new menu prompt

def requiredLine():                 # to print the required line in a less messy way
    print(f"{"Name":20}{"League":>10}{"Goals":>10}{"Assists":>10}{"Passes":>10}")

playerList = initialize()
while True:
    display_menu()
    option=input("Enter Command: ")
    
    if option =="1":
        requiredLine()
        for playerX in playerList:      # easy way to list all players
            playerX.listPlayers()
        print("")                       # provide a newline for the new menu prompt
        
    if option =="2":
        min_goals=int(input("Please indicate number of goals: "))
        if min_goals <= 30:                     # dont print if variable > 30
            requiredLine()
        display_goal(min_goals)
        print("")                               # provide a newline for the new menu prompt      
#check for invalid user input ie text or negative num with while loop
    if option =="3":
        selected_league=input("Please indicate the league: ")
        if selected_league == "EPL" or selected_league == "Bundesliga" or selected_league == "La Liga":
            requiredLine()                          # only print for valid leagues
        display_league(selected_league)
        print("")                                   # provide a newline for the new menu prompt
   #check for invalid user input by adding else statement and tabbing other thing in
    if option =="4":
        selected_player=input("Please indicate name of player: ")
        for i in range(10):
            player = playerList[i]                  # check if name exists, if it does, print out name/league...
            if player.name == selected_player:
                requiredLine()                      # only print if the player name is in the list
        display_player(selected_player)
        print("")                                   # provide a newline for the new menu prompt
    # check for number input
    if option =="5":
        display_most_goals()
    
    if option =="6":
        calculate_total_points()

    if option =="7":
        print("Exiting")  # if they want to exit, break
        break
