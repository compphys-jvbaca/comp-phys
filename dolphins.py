"""

A Dolphin Population Model
Due 11pm on Thursday, Oct. 15, 2015

Name: Jacob Baca
Partner: Terry Tran

Build a model for a dolohin population over 150 years

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
        self.timeafter = True
        print self.name + ' was created'
        
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
        if type(self.timeafter) != bool:
            if self.timeafter <= 5:
                return False
        if self.sex == Dolphin.sex: #can't have the same sex
            return False 
        if (self.age < 8) or (Dolphin.age < 8): #above age of 8
            return False 
        if abs(self.age - Dolphin.age) >= 10: #no age difference greater than 10
            return False
        if (Dolphin.mother,Dolphin.father) == (self.mother,self.father):
            return False
        else:
            return True

################################################################################################################################################

def name_generator(sex):
    male_name_lst = []
    female_name_lst = []
    z = 0 #number of pages iterated through

    while z <=1: #iterates through baby-names website pages for names 

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

    female_names = []
    for name in female_name_lst: #same as above
        string = name.lstrip('ils">').rstrip('</s')
        female_names.append(string)

    #print female_names[20]
    
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
            
male_generator = name_generator('male')
female_generator = name_generator('female')

def creation(mother, father):
    if Dolphins.sexy_time(mother, father):
        gender = random.random([male, female])
        print gender
        if gender == 'male':
            male_gener = male_generator.next()
            print male_gener
            male_gener = Dolphins(male_gener, mother, father, gender)
        else:
            female_gener = female_generator.next()
            female_gener = Dolphins(female_gener, mother, father, gender)
            
        mother.timeafter = 0
        father.timeafter = 0
    else:
        print 'Cannot procreate.'

#these are the original 4 dolphin in the population:
Jeffery = Dolphins('Jeffery', 'Todd Pinkins', 'Hilay sause', 'male')
Carrot = Dolphins('Carrot', 'Too Pin', 'Hilary Fartse', 'male')
Kayak = Dolphins('Kayak', 'Td kins', 'Hiary tersause', 'female')
Tiffany = Dolphins('Tiffany', 'dd Pis', 'Hil Fase', 'female')

m_dolph_dic={'Jeffery':Jeffery, 'Carrot':Carrot}
f_dolph_dic={'Kayak':Kayak, 'Tiffany':Tiffany}
dead_dolph_dic={}

for i in range(151):
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
    
    for male in m_dolp_dic:
        for female in f_dolp_dic:
            
    print dolph_dic.keys()
            
        #print Jeffery.age, Carrot.age, Kayak.age, Tiffany.age