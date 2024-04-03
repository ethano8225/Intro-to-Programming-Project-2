####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34260003

""" Implement the main program and functions below """
import Player 

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
        if  player_being_checked.goals >= user_input:   # only print if player goals is greater than user input
            player_being_checked.listPlayers()
        elif user_input>30:                             # no player has more than 30 goals, print if 
            print("No players found.")                  # user input > 30
            break
            
def display_league(user_input):
    count = 0
    for i in range(10):                         # displays players with specific league,
        checking_league=playerList[i]           # and checks to see if none are printed to say
        count = count + 1                       # no players found, if needed.
        if checking_league.league == user_input:
            count =  count - 1
            checking_league.listPlayers()
        elif count == 10:
            print("No players found.")
            break

def display_player(user_input):
    a=0
    for i in range(10):
        checking_player=playerList[i]
        a=a+1
        if checking_player.name == user_input:      # for loop to go through all the players
            checking_player.listPlayers()           # and check if the name matches.
            a=a-1                                   # also keeps track if no players were printed
        elif a==10:
            print("No players found.")
        
def display_most_goals():
    best_players_goals=0
    for i in range(10):
        player_being_checked=playerList[i]                      # for loop to go through players.
        if player_being_checked.goals > best_players_goals:     # Set bestPlayerGoals to a higher value if that player
            best_players_goals=player_being_checked.goals       # has more goals.
    for i in range (10):
        player_being_checked2 = playerList[i]                   # print out the player that matches that amount
        if best_players_goals == player_being_checked2.goals:   # of goals
            print(f"{player_being_checked2.name} has the most goals with {player_being_checked2.goals}.\n")
    
def calculate_total_points():
    for i in range(10):
        pl=playerList[i]                                      # goals = 2.5 pts per, assists is .93 per, passes are .05 per.
        total_points= float(pl.goals) * 2.5 + float(pl.assists)*.93 + float(pl.passes) * .05
        total_points_rounded=round(total_points,2)
        print(f"{pl.name} has {total_points_rounded} points.") # print out the player with x amount of fantasy points.
    print("")       #provide a newline for the new menu prompt
        

while True:
    display_menu()
    option=input("Enter Command: ")
    
    if option =="1":
        print("Name   \t\t\tLeague\t\tGoals\t\tAssists\t\tPasses")
        for i in playerList:  # easy way to list all players
            i.listPlayers()
        print("")       #provide a newline for the new menu prompt
        
    if option =="2":
        min_num_of_goals=int(input("Please indicate number of goals: "))
        if min_num_of_goals <= 30:              # no players have more than 30 goals, dont print if variable > 30
            print("Name   \t\t\tLeague\t\tGoals\t\tAssists\t\tPasses")
        display_goal(min_num_of_goals)
        print("")       #provide a newline for the new menu prompt      

    if option =="3":
        selected_league=input("Please indicate the league: ")
        if selected_league == "EPL" or selected_league == "Bundesliga" or selected_league == "La Liga":
            print("Name   \t\t\tLeague\t\tGoals\t\tAssists\t\tPasses")      # only print for valid leagues
        display_league(selected_league)
        print("")      #provide a newline for the new menu prompt
   
    if option =="4":
        selected_player=input("Please indicate name of player: ")
        for i in range(10):
            player = playerList[i]                          # check if name exists, if it does, print out name/league...
            if player.name == selected_player:
                print("Name   \t\t\tLeague\t\tGoals\t\tAssists\t\tPasses") # only print if the player name is in the list
        display_player(selected_player)
        print("")      #provide a newline for the new menu prompt
    
    if option =="5":
        display_most_goals()
    
    if option =="6":
        calculate_total_points()

    if option =="7":
        print("Exiting")  # if they want to exit, break
        break
