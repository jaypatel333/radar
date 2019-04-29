from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re


def trends_JSON():
	############################ Pulls Data ##########################
	driver = webdriver.Chrome('C:/Users/tazma/Documents/TopicRadar/chromedriver')
	# this is for realtime
	# https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all

	#This is for daliy content
	driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')
	#driver.get('https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all')
	#grabs raw html
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	driver.quit()
	#########################################################


	#grabs content puts it in a dict
	Trend_JSON = []

	for x in soup.find_all('div', class_='feed-item contracted-item'):
	    title = re.sub(r'\s+', ' ',x.find(class_='title').text).strip()
	    summary = x.find(class_='summary-text').text.strip()
	    link = x.findAll('a', href=True)[1]["href"]
	    source = x.find(class_='source-and-time').text.strip()
	    search_count = x.find(class_='search-count-title').text
	    date = x.find_all_previous('div', class_='content-header-title')[0].text
	    temp_dict = {'Link':link,  'Searches':search_count,'Source':source,'Summary':summary, 'Title':title, 'Date':date}
	    Trend_JSON.append(temp_dict)
		

	return Trend_JSON
	
def trends_ONLY_JSON():
	############################ Pulls Data ##########################
	driver = webdriver.Chrome('C:/Users/tazma/Documents/TopicRadar/chromedriver')
	#driver = webdriver.Chrome('C:/Users/Allen/Desktop/TopicRadar/chromedriver')
	# this is for realtime
	# https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all

	#This is for daliy content
	driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')
    #driver.get('https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all')
	#grabs raw html
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	driver.quit()
	#########################################################


	#grabs content puts it in a dict
	Trend_JSON = []

	for x in soup.find_all('div', class_='feed-item contracted-item'):
		title = re.sub(r'\s+', ' ',x.find(class_='title').text).strip()
		title = title.replace("•", "")
	    #summary = x.find(class_='summary-text').text.strip()
	    #link = x.findAll('a', href=True)[1]["href"]
	    #source = x.find(class_='source-and-time').text.strip()
	    #search_count = x.find(class_='search-count-title').text
	    #date = x.find_all_previous('div', class_='content-header-title')[0].text
		temp_dict = {'Title':title}
		Trend_JSON.append(temp_dict)
	print(Trend_JSON)

	return Trend_JSON
	
def trends_ONLY_JSON(RC):
	############################ Pulls Data ##########################
	#driver = webdriver.Chrome('C:/Users/tazma/Documents/TopicRadar/chromedriver')
	driver = webdriver.Chrome('C:/Users/jaypa/Desktop/UNCC/4155capston/radar/TopicRadar/chromedriver')
	# this is for realtime
	# https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all

	#This is for daliy content
	driver.get('https://trends.google.com/trends/trendingsearches/realtime?geo='+RC+'&category=all')
    #driver.get('https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all')
	#grabs raw html
	html = driver.page_source
	soup = BeautifulSoup(html, 'html.parser')
	driver.quit()
	#########################################################


	#grabs content puts it in a dict
	Trend_JSON = []
	id = 0
	for x in soup.find_all('div', class_='feed-item contracted-item'):
		title = re.sub(r'\s+', ' ',x.find(class_='title').text).strip()
		title = title.replace("•", "")
		trend_id = id
		id = id + 1
	    #summary = x.find(class_='summary-text').text.strip()
	    #link = x.findAll('a', href=True)[1]["href"]
	    #source = x.find(class_='source-and-time').text.strip()
	    #search_count = x.find(class_='search-count-title').text
	    #date = x.find_all_previous('div', class_='content-header-title')[0].text
		temp_dict = {'Title':title, 'Trend_id' : trend_id}
		Trend_JSON.append(temp_dict)

	return Trend_JSON
	
	



##driver = webdriver.Chrome('C:/Users/tazma/Documents/TopicRader/chromedriver')

# this is for realtime
# https://trends.google.com/trends/trendingsearches/realtime?geo=US&category=all

#This is for daliy content
##driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')

#grabs raw html
##html = driver.page_source
##soup = BeautifulSoup(html, 'html.parser')
##driver.quit()


##def grabbing(soup):
	#grabs content puts it in a dict
##	master_dict=[]

	##for x in soup.find_all('div', class_='feed-item contracted-item'):
	  ##  title = re.sub(r'\s+', ' ',x.find(class_='title').text).strip()
	   ## summary = x.find(class_='summary-text').text.strip()
	   ## link = x.findAll('a', href=True)[1]["href"]
	   ##source = x.find(class_='source-and-time').text.strip()
	    ##search_count = x.find(class_='search-count-title').text
	    ##date = x.find_all_previous('div', class_='content-header-title')[0].text
	    ##temp_dict = {'Link':link,  'Searches':search_count,'Source':source,'Summary':summary, 'Title':title, 'Date':date}
	    ##master_dict.append(temp_dict)

	##return master_dict

##master_dict = grabbing(soup)

##df = pd.DataFrame.from_dict(master_dict)

##df.to_csv('export.csv', encoding='utf-8')

##print('an export has been created')
