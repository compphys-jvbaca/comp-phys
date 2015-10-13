import urllib2 
import re

def download_names():
	male_name_lst = []
	female_name_lst = []
	z = 0 #number of pages iterated through

	while z <=50: #iterates through baby-names website pages for names 

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
		#print female_text
		
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

	female_names = []
	for name in female_name_lst: #same as above
		string = name.lstrip('ils">').rstrip('</s')
		female_names.append(string)

	a = open('woman_names', 'w') 
	b = open('man_names', 'w')

	a.write(str(female_names))
	b.write(str(male_names))

	a.close()
	b.close()
	
	#with open('woman_names', 'r') as f:
		#print f.read()

