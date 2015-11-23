'''Terry and Jacob's program that provides output of the perfect date based on a series of input such as the following:

1. Staying in vs. going out
2. Local vs. travel
3. Food........!!!!!!!!!!!!!!!!!
4. Movies......!!!!!!!!!!!!!!!!!
5. Etc., etc., etc.

'''

Dates_Dictionary = {}	#contains all date instances created by Terry and Jacob 

class Dates: #creates a date instance with attributes such as budget, location, and type  
    
    def __init__(self, name, type, cost, location, description):
        self.name = name
		self.type = type #food, movie, date, or travel
		self.cost = cost #max amount of money date will cost
		self.location = location #at home or somewhere else
		self.description = description # short description for more details
		
		Dates_Dictionary[self.name] = self #automatically adds instance to Dates_Dictionary upon creation of date 
    
	# def food(self, delivery == True):
        # if delivery == True:
            # #spit out delivery options
        
        # else:
            # #spit out dine out options
            
    # def movies(self, genre): #determines specific movie 
    
    # def travel(self, local = True): #determines a local or far off destination



Wes_Anderson = Dates('date', 20, home, str(Watch all Wes Anderson films: http://www.imdb.com/name/nm0027572/ (imdb discography). We would need popcorn and snacks as well...))


def Date_Conversation(): #determines which date to go on  
	date_type = raw_input('What do you want to do? Eat or watch a movie or go on a date or travel. (Enter eat,movie,date,or travel or any if you cannot decide): '))
	location = raw_input('Do you want to go out or stay in? (Enter out or in): )
	cost = float(raw_input('How much do you want to spend? (Enter a number from 0 to infinity): )) #cost is type float 
	
	################################################################
	
	#before looking at the daate_type we should sort through the
	#Dates_Dictionary by location and cost and put into a list to
	#reduce the indexing later on this will save us time and allow
	#the program to run faster
	
	################################################################
	
	if date_type == 'eat':
		#sort through dictionary for restaraunt types
	if date_type == 'movie':
		#sort through dictionary for movie types
	if date_type == 'date':
		#sort through dictionary for date types
	if date_type == 'travel':
		#sort through dictionary for travel types
	else:
		#selects a date completely randomly
		
	
