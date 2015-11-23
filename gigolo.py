'''Terry and Jacob's program that provides output of the perfect date based on a series of input such as the following:

1. Staying in vs. going out
2. Local vs. travel
3. Food........!!!!!!!!!!!!!!!!!
4. Movies......!!!!!!!!!!!!!!!!!
5. Etc., etc., etc.

'''

class Dates: #creates a date instance with attributes such as budget, location, and type  
    
    def __init__(self, type, cost, location):
        self.type = type #food, movie, date, or travel
		self.cost = cost #max amount of money date will cost
		self.location = location #where it is located
    
    # def food(self, delivery == True):
        # if delivery == True:
            # #spit out delivery options
        
        # else:
            # #spit out dine out options
            
    # def movies(self, genre): #determines specific movie 
    
    # def travel(self, local = True): #determines a local or far off destination

Dates_Dictionary = {}	#contains all date instances created by Terry and Jacob 

def Date_Conversation(): #determines which module to use 
	date_type = raw_input('What do you want to do? Eat or watch a movie or go on a date or travel. (Enter eat,movie,date,or travel): '))
	if date_type = 'eat':
		#sort through dictionary for restaraunt types
	if date_type = 'movie':
		#sort through dictionary for movie types
	if date_type = 'date':
		#sort through dictionary for date types
	if date_type = 'travel':
		#sort through dictionary for travel types
		
	
