#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

def getNewsSources(TrendsList):
	master_dict=[]
	
	
	#UPDATE CHROMEDRIVER LOCATION TO SERVER LOCATION
	#driver = webdriver.Chrome('C:/Users/tazma/Documents/TopicRadar/chromedriver')
	driver = webdriver.Chrome('C:/Users/jaypa/Desktop/UNCC/4155capston/radar/TopicRadar/chromedriver')

	for x in TrendsList:
		#x = x['Title']
		driver.get("https://cse.google.com/cse?cx=004341253442084066054:hqcqt8c54li")
		text_area= driver.find_element_by_id("gsc-i-id1")
		text_area.send_keys(x['Title']+ "\n")

		#print("waiting for shit to load")
		time.sleep(2)
		#grabs raw html
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')

		def grabbing(soup, x):
			#grabs content puts it in a dict
			master_dict=[]
			#holds transfer topic to local val for later storage in dict
			trend=x['Title']
			trend_id= x['Trend_id']
			length_check = 0
			id = 0
			print("grabbing some soup")
			
			for y in soup.find_all('div', class_="gs-webResult gs-result")[:10]:
				article_id = id
				id = id + 1
				length_check = length_check + 1
				title = y.find('a',class_="gs-title").text.strip()
				#link = y.find('div', class_="gs-bidi-start-align gs-visibleUrl gs-visibleUrl-long").text.strip()
				
				# Added to stop the error of no Heaf
				try:
					link = y.find('a', class_="gs-title")['href']
				except KeyError:
					link = ""
				#end added error
				sep = '...'
				article_date = y.find(class_='gs-bidi-start-align gs-snippet').text
				article_date = article_date.split(sep, 1)[0]
				
				 
				art = str(y.find('img', class_="gs-image"))
				sep=" src="
					 
				if art.strip(): # strip will remove all leading and trailing whitespace such as '\n' or ' ' by default    
					art_image = art.strip("\n ' '")
					
				try:art =(str(art).rsplit(sep, 1)[1])
				#Got tired of trying to format the syntax for when the style=none>
				except: art="No image found"
						
				temp_dict = {'Article_id':article_id, 'Title':title, 'Trend':trend,'Trend_id':trend_id ,'URL':link, 'post_date':article_date,'Thumbnail':art}
				master_dict.append(temp_dict)
			while length_check < 10:
				length_check = length_check + 1
				article_id = id
				id = id + 1
				title = ''
				link = ''
				article_date = ''
				art = ''
				temp_dict = {'Article_id':article_id, 'Title':title, 'Trend':trend,'Trend_id':trend_id ,'URL':link, 'post_date':article_date,'Thumbnail':art}
				master_dict.append(temp_dict)
			return master_dict
		#Keeps the dict updated with info from new topic
		master_dict= master_dict + grabbing(soup,x)
	driver.quit()
	print("killed chrome sucessfull")
	print(master_dict)
	
	return master_dict