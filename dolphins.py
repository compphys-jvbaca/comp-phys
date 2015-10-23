"""

A Dolphin Population Model
Due 11pm on Thursday, Oct. 15, 2015

Name: Jacob Baca
Partner: Terry Tran

Build a model for a dolohin population over 150 years. This will take a while
to run because I am creating the list of names each trial. Sorry! I will change
it in part B

"""

import random 
import math
import urllib2 
import re


t = 0

class Dolphins:
    
    def __init__(self, name, mother, father, sex):
        self.name = name
        self.mother = mother
        self.father = father
        self.sex = sex
        self.death = random.gauss(35, 5)
        self.age = 0
        self.timeafter = True #time after procreating 
        #print self.name + ' was created'
        
    def aging(self):
        self.age += 1
        if type(self.timeafter) == int:
            self.timeafter+=1
            if self.timeafter > 5:
                self.timeafter = True
        return self.age
    
    
    
    def die(self):
        #print self.age, int(self.death)
        if self.age == int(self.death):
            return True
        else : 
            return False
    
    def sexy_time(self, Dolphin):
        #print self.name, self.timeafter, Dolphin.name, Dolphin.timeafter
        if type(self.timeafter) != bool:
            if self.timeafter <= 5:
                return False
        if self.sex == Dolphin.sex: #can't have the same sex
            return False 
        if (self.age < 9) or (Dolphin.age < 9): #above age of 8
            return False 
        if abs(self.age - Dolphin.age) >= 10: #no age difference greater than 10
            return False
        if (Dolphin.mother,Dolphin.father) == (self.mother,self.father):
            return False
        
        #restricts them from mating with their parents. 
        if self.mother == Dolphin.name or self.father == Dolphin.name:
            return False
        if Dolphin.mother == self.name or Dolphin.father == self.name:
            return False
        else:
            return True

################################################################################################################################################

def name_generator(sex):
    male_name_lst = []
    female_name_lst = []
    z = 0 #number of pages iterated through

    while z <=100: #iterates through baby-names website pages for names 

        m_names = 'http://www.prokerala.com/kids/baby-names/boy/page-' + str(z) + '.html'
        f_names = 'http://www.prokerala.com/kids/baby-names/girl/page-' + str(z) + '.html'
        
        #male names
        infile = urllib2.urlopen(m_names) 
        male_text = infile.read()   
        infile.close() 
        #print male_text

        #female names
        infile = urllib2.urlopen(f_names) 
        female_text = infile.read()   
        infile.close() 

        #finds all names and puts in list
        male_name_lst_temp = re.findall('ils">.*</s', male_text)
        male_name_lst += male_name_lst_temp
        female_name_lst_temp = re.findall('ils">.*</s', female_text)
        female_name_lst += female_name_lst_temp

        z+=1

    male_names = []
    for name in male_name_lst: # strips names of unnecessary characters
        string = name.lstrip('ils">').rstrip('</s')
        male_names.append(string)

    #print male_names
    random.shuffle(male_names)

    female_names = []
    for name in female_name_lst: #same as above
        string = name.lstrip('ils">').rstrip('</s')
        female_names.append(string)
    
    #print female_names[20]
    random.shuffle(female_names)
    
    m=0
    f=0
    if sex == 'male':
        while m < len(male_names):
            yield male_names[m]
            m+=1

    if sex == 'female':
        while f< len(female_names):
            yield female_names[f]
            f+=1

###################################################################################################################            
    
def creation(mother, father):
    if mother.sexy_time(father):
        gender = random.choice(['male', 'female'])
        #print gender
        if gender == 'male':
            male_gener = male_generator.next()
            #print male_gener
            male_babyboy = Dolphins(male_gener, mother, father, gender) #creates instance
            mother.timeafter = 0
            father.timeafter = 0
            return male_babyboy
            #m_dolph_dic[male_babyboy.name] = male_babyboy
        else:
            female_gener = female_generator.next()
            female_babygurl = Dolphins(female_gener, mother, father, gender) #creates instance
            mother.timeafter = 0
            father.timeafter = 0
            return female_babygurl
            #f_dolph_dic[female_babygurl.name] = female_babygurl

#these are the original 4 dolphin in the population:
Jeffery = Dolphins('Jeffery', 'Todd Pinkins', 'Hilay sause', 'male')
Carrot = Dolphins('Carrot', 'Too Pin', 'Hilary Fartse', 'male')
Kayak = Dolphins('Kayak', 'Td kins', 'Hiary tersause', 'female')
Tiffany = Dolphins('Tiffany', 'dd Pis', 'Hil Fase', 'female')

m_dolph_dic={'Jeffery':Jeffery, 'Carrot':Carrot}
f_dolph_dic={'Kayak':Kayak, 'Tiffany':Tiffany}
dead_dolph_dic={}

print 'running...'
for i in range(1, 11):
    
    print 'Trial No. ', i
    
    male_generator = name_generator('male')
    female_generator = name_generator('female')
    
    for t in range(150): #this progresses through 150 years
        if t==0 or t==25 or t==50 or t==75 or t==100 or t==125:
            print '#####################################################',\
                  '\n', 'Entering Year: ', t, 'with',\
                  len(m_dolph_dic.keys()) + len(f_dolph_dic.keys()),\
                'dolphins,', 'with', 'num', 'breeding.'

        if t==149:
            print '#####################################################',\
                  '\n','At year', t, ', there are ',\
                  len(m_dolph_dic.keys()) + len(f_dolph_dic.keys()),\
                'living dolphins.'
        lst = []

        #male age dolphins
        for dolphin in m_dolph_dic: #Ages dolphins and checks if they are at the age of death
            #print dolphin
            dol = m_dolph_dic[str(dolphin)]
            dol.aging()
            #print 'dol.die() = ', dol.die(),int(dol.death), dol.age
            if dol.die() == True:
                lst.append(dol)

        for dolphin in lst: #deletes dolphins from dictionary and adds to dead dolph dictionary
            dead_dolph_dic[dolphin.name]=dolphin
            del m_dolph_dic[dolphin.name]

        lst = []

        #female Age dolphins
        for dolphin in f_dolph_dic: #Ages dolphins and checks if they are at the age of death
            #print dolphin
            dol = f_dolph_dic[str(dolphin)]
            dol.aging()
            #print 'dol.die() = ', dol.die(),int(dol.death), dol.age
            if dol.die() == True:
                lst.append(dol)

        for dolphin in lst: #deletes dolphins from dictionary and adds to dead dolph dictionary
            dead_dolph_dic[dolphin.name]=dolphin
            del f_dolph_dic[dolphin.name]

        baby_dolphins = []

        for male in m_dolph_dic: #mates dolphin population
            for female in f_dolph_dic: 
                baby = creation(m_dolph_dic[male], f_dolph_dic[female])
                if isinstance(baby, Dolphins): #check if it is the string 'cannot procreate' or a dolphin instance if it is 
                    baby_dolphins.append(baby)

        for dolphin in baby_dolphins: #adds newly born dolphins to living dolphin lists
            if dolphin.sex == 'male':
                m_dolph_dic[dolphin.name]= dolphin
            else:
                f_dolph_dic[dolphin.name]= dolphin
                
    m_dolph_dic={'Jeffery':Jeffery, 'Carrot':Carrot} #restarting the dics
    f_dolph_dic={'Kayak':Kayak, 'Tiffany':Tiffany}
    dead_dolph_dic={}
    
    print 'n\', "***************************************************************", 'n\'
    