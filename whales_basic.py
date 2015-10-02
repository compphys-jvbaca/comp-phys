import datetime as dt
import random 

class Whale:
    
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self.born = dt.datetime.now()
        print 'A ' + str(self.sex) + ' whale named ' + str(self.name) + ' was born!'
        
    def __call__(self):
        return '\n'
    
    def __str__(self):
        return 'A whale named ' + str(self.name) + ' ' + str(dt.datetime.now() - self.born)
    
    def sing(self):
        return '\a \a \a \a \a'
    
    def age(self):
        age = dt.datetime.now() - self.born   
        return age


names = ['zowshung', 'carrots', 'enter the huang', 'mothra and huang', 'james and the giant huang',\
         'die huang', 'master shifu', 'xiaothonic', 'xiaosheng soccer', 'Huangfu Hustle',\
         'Xiaouching tiger hidden huang', 'shanghuang noon', 'mortal huangbat',\
         'Huang Potter and the prisoner of Huangkaban', 'The Huang strikes back', 'The Hobbit:\
Desolation of Huang', 'The Huanger Games', 'Willy Hwongka and the Chocosheng Factory',\
	 'Iron Huang', 'Xiaosheng']   


gender = ['female', 'male']

for n in names:
    random.shuffle(gender)
    n = Whale(n , gender[0])
 