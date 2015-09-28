'''

Homework 4: flight_schedule.py
Name : Jacob Baca
Partner : Terry Tran

For this part, the following Python built-in methods 
(for lists) and statements may help you:
.sort(), .insert(), .append()
continue, break (typically used in a loop)
In printing, consider using \t for tab.

'''

airports = {"DCA": "Washington, D.C.", "IAD": "Dulles", \
"LHR": "London-Heathrow", "SVO": "Moscow", \
"CDA": "Chicago-Midway", "SBA": "Santa Barbara", \
"LAX": "Los Angeles","JFK": "New York City", \
"MIA": "Miami", "AUM": "Austin, Minnesota"}

# airline, number, heading to, gate, time (decimal hours)
flights = [("Southwest",145,"DCA",1,6.00),\
("United",31,"IAD",1,7.1),("United",302,"LHR",5,6.5),\
("Aeroflot",34,"SVO",5,9.00),("Southwest",146,"CDA",1,9.60),\
("United",46,"LAX",5,6.5), ("Southwest",23,"SBA",6,12.5),\
("United",2,"LAX",10,12.5),("Southwest",59,"LAX",11,14.5),\
("American", 1,"JFK",12,11.3),("USAirways", 8,"MIA",20,13.1),\
("United",2032,"MIA",21,15.1),("SpamAir",1,"AUM",42,14.4)]

airline_sort = sorted(flights) #sort flights list
print 'Flight \t', 'Destination \t', 'Gate \t', 'Time'
print '------------------------------------'
for f in flights:
	print f[0],f[1], '\t', airports[f[2]], '\t', f[3], '\t', f[4], '\t'  
print airline_sort


time_sort = sorted(flights, key = lambda f : f[4]) #sort time list
print '\n', time_sort


