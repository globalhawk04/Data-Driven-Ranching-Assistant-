#this is an example calculator

days_of_feed = input(' how many days of feed do you want to buy ')

lactation = input('how many lactation cows do you have ')

#lac_move = input('how much do they move est in km ')

lac_milk = input('how much milk are they making ')

lac_weght = input('how do they weigh ')

lac_day = input('how long they been milking ')

lac_par = input ('how many times cow has given birth ')

growing = input('how many growing cows do you have ')

#grow_move = ('how much do they move est in km ')

grow_weight = input('how do they weigh ')

calves = input('how many calves do you have ')

#calve_move = ('how much do they move est in km ')

calve_weigh = input('how do they weigh ')

pregnant = input('how many pregnatn cows do you have ')

#preg_move = input('how much do they move est in km ')

preg_weigh = input('how do they weigh ')


dmi_lac= ((3.7 + int(lac_par)  * 5.7) + .305 * 624 + .022 * int(lac_weght)  + (-.689 - 1.87 * int(lac_par )) * 3) * (1 - (2.12 + int(lac_par)  * .136)**(-.053*int(lac_day)))


print('lactation cows need an estimated dmi pounds of ')
dmi_lac_needed = dmi_lac*2.22*int(lactation)

dmi_grow = .022 * 700* (1**(-1.54*(int(grow_weight)/1500)))

print('growing cows need an estimated dmi pounds of ')

dmi_grow_needed = dmi_grow*2.22*int(growing)

calv_dmi = -652.525 +(int(calve_weigh)*14.734)+(0.882*18.896)+(2*73.303)+((2**2) * 13.496) - (29.614 * 2 *0.882)

print('calves need an estimated dmi pounds of ')

calv_dmi_needed = (calv_dmi*0.00220462*int(calves))*(int(days_of_feed))

preg_dmi = 1.47 - ((.365 -.0028*30)*8)-.035*3**2

print('pregnant cows need an estimated dmi pounds of ')

final_preg = -1 * preg_dmi*12*2.22*int(pregnant)

print('you need an estimate all feed DMI of ')

all_feed_needed = (dmi_lac_needed+dmi_grow_needed+final_preg)*(int(days_of_feed))
print(all_feed_needed)


print('you need an estimate all calf DMI of ')
print(calv_dmi_needed)



import requests
from bs4 import BeautifulSoup as soup
import webbrowser
import os
from urllib.request import Request, urlopen
import pandas as pd
import time
import csv
import json 


websiteurl = 'https://shop.berendbros.com/departments/calf-|70|P35|P351.html'

websiteurl_1 = 'https://shop.berendbros.com/departments/bags-|70|P35|P352.html'

websiteurl_2 = 'https://shop.berendbros.com/departments/supplements-|70|P35|P353.html?top=0'

websiteurl_3 = 'https://shop.berendbros.com/departments/supplements-|70|P35|P353.html?top=15'

other_links = []

calf_name = []
calf_feed = []
calf_price = []


all_feed_name = []
all_feed = [50,50,50,50,50,50,50,50,50,50,40]
all_feed_price = []

#print(websiteurl)
try:
	req = Request(websiteurl, headers={"User-Agent": 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soups = soup(webpage,'html.parser')
	#print(soups)
	for link in soups.find_all('div', class_ = 'card-body'):
		for product in link.find_all ('div', class_ = 'product_link'):
			#print(product.text)
			calf_feed.append(50)
			calf_name.append(product.text)

		for price in link.find_all('div', class_ = 'product_price'):
			#print(price.text)

			calf_price.append(price.text)
    #for link in soups.find_all('h1'):
        #print(link.text)
	#print(calf_feed)
	calf_price= [x.strip() for x in calf_price]
	calf_price= [x.strip('$') for x in calf_price]
	calf_price = [float(x) for x in calf_price]
	#print(calf_feed)
	#print(calf_price)
#print(websiteurl)

	req = Request(websiteurl_1,headers={"User-Agent": 'Mozilla/5.0'})
	webpage = urlopen(req).read()
	soups = soup(webpage,'html.parser')
	#print(soups)
	for link in soups.find_all('div', class_ = 'card-body'):
		for product in link.find_all ('div', class_ = 'product_link'):
			#print(product.text)
			all_feed_name.append(product.text)
			#pass

		for price in link.find_all('div', class_ = 'product_price'):
			#print(price.text)
			all_feed_price.append(price.text)

	all_feed_price= [x.strip() for x in all_feed_price]
	all_feed_price= [x.strip('$') for x in all_feed_price]
	all_feed_price = [float(x) for x in all_feed_price]
	#print(all_feed)
	#print(all_feed_price)
    #for link in soups.find_all('h1'):
        #print(link.text)

    #for link in soups.find_all('h1'):
        #print(link.text)

except Exception as e:
	print(e)

sorted_all_feed = []
sorted_calf_feed = []

print(all_feed)
for x in range(0,len(all_feed)):
	#print(x)
	print(all_feed_name[x])
	z = all_feed_needed/ all_feed[x]
	print('you need this many bags of feed ' + str(z))
	print('price of this feed is ')
	print(all_feed_price[x])
	print('total cost of this feed is ')
	print(z * all_feed_price[x])
	cost = z * all_feed_price[x]
	name = all_feed_name[x]
	sorted_all_feed.append((name,cost))
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

for x in range(0,len(calf_name)):
	#print(x)
	print(calf_name[x])
	z = calv_dmi_needed / calf_feed[x]
	print('you need this many bags of feed ' + str(z))
	print('price of this feed is ')
	print(calf_price[x])
	print('total cost of this feed is ')
	print(z * calf_price[x])
	cost = z * calf_price[x]
	name = calf_name[x]
	sorted_calf_feed.append((name,cost))
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
	print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#print(sorted_calf_feed)

sorted_calf_feed.sort(key = lambda x: x[1])

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

print('your cheapest calf option is ')
print(sorted_calf_feed[0])

print('your most expensive calf option is ')
print(sorted_calf_feed[-1])

print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

#print(sorted_all_feed)

sorted_all_feed.sort(key = lambda x: x[1])


print('your cheapest all_feed option is ')
print(sorted_all_feed[0])

print('your most expensive all feed option is ')
print(sorted_all_feed[-1])
