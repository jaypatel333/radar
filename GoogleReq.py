from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome(executable_path='https://github.com/jaypatel333/radar/blob/master/chromedriver')

driver.get('https://trends.google.com/trends/trendingsearches/daily?geo=US')

#grabs raw html
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
driver.quit()

def grabbing(soup):
	#grabs content puts it in a dict
	master_dict=[]

	for x in soup.find_all('div', class_='feed-item contracted-item'):
	    title = re.sub(r'\s+', ' ',x.find(class_='title').text).strip()
	    summary = x.find(class_='summary-text').text.strip()
	    link = x.findAll('a', href=True)[1]["href"]
	    source = x.find(class_='source-and-time').text.strip()
	    search_count = x.find(class_='search-count-title').text
	    date = x.find_all_previous('div', class_='content-header-title')[0].text
	    temp_dict = {'Link':link,  'Searches':search_count,'Source':source,'Summary':summary, 'Title':title, 'Date':date}
	    master_dict.append(temp_dict)

	return master_dict

master_dict = grabbing(soup)

df = pd.DataFrame.from_dict(master_dict)

df.to_csv('export.csv', encoding='utf-8')

print('an export has been created')
