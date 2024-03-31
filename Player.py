####### Names and Spire ID ###########
# 1. Ethan O'Connor 34445111
# 2. Ryan Blanchette 34620003

""" Implement the Player class and functions below """

class Player:
    def __init__(self,name,league,goals,assists,passes):
        self.name = name
        self.league = league
        self.goals = goals
        self.assists = assists
        self.passes = passes
    def listPlayers(self):
        if len(self.name) <= 17 and len(self.name) > 10:
            text = "{0:<0}\t\t{1:>6}\t{2:>13}{3:>18}\t{4:>14}".format(self.name,self.league,self.goals,self.assists,self.passes)
        if len(self.name) == 10:
            text = "{0:<0}{1:>20}\t{2:>13}{3:>18}\t{4:>14}".format(self.name,self.league,self.goals,self.assists,self.passes)
        if len(self.name) > 17:
            text = "{0:<0}{1:>12}\t{2:>13}{3:>18}\t{4:>14}".format(self.name,self.league,self.goals,self.assists,self.passes)
        if len(self.name) == 15 and len(self.league) == 7:
            text =  "{0:<0}\t{1:>14}\t{2:>13}{3:>18}\t{4:>14}".format(self.name,self.league,self.goals,self.assists,self.passes)
        if len(self.name) == 15 and len(self.league) == 10:
            text = "{0:<0}\t{1:>14}\t{2:>13}{3:>18}\t{4:>14}".format(self.name,self.league,self.goals,self.assists,self.passes)
        print(text)



        #if len(self.name) <= 15 and len(self.league) < 7:
        #                                                      # must check the length of the each string to allow for 
        #    print(self.name,"",self.league,"",self.goals,self.assists,self.passes,"1",sep="\t")  # good looking formatting
        #elif len(self.name) <= 15 and len(self.league) > 7:
        #    print(self.name,"",self.league,self.goals,self.assists,self.passes,"2",sep="\t")        
        #elif len(self.name) > 15 and len(self.league) >= 7:                                                   
        #    print(self.name,self.league,"",self.goals,self.assists,self.passes,"3",sep="\t")
        #elif len(self.name) <= 15 and len(self.league) == 7:
        #    print(self.name,"",self.league,"",self.goals,self.assists,self.passes,"4",sep="\t")  

        #else:
        #    print(self.name,"\t",self.league,self.goals,self.assists,self.passes,sep="\t")
    


