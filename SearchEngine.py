#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
import re
import time

#creates a dict to load topic data from export
title_list=[]
master_dict=[]
#opens export file and loads topic data
temp=pd.read_csv('export.csv', usecols=[6], nrows=10)#change nrows for total topics

#stores topics into a list
title_list=temp.values.tolist()
print(title_list)

#removes previous formatting and stores clean text
for x in title_list:
    
    title_list=str(title_list)
    title_list=title_list.replace("[['", "")
    title_list=title_list.replace("['", "")
    title_list=title_list.replace("']]", "")
    title_list=title_list.replace("']", "")

title_list=title_list.split(', ')

#UPDATE CHROMEDRIVER LOCATION TO SERVER LOCATION
driver = webdriver.Chrome(executable_path='/Users/Nicky/Downloads/chromedriver')


for x in title_list:
    driver.get("https://cse.google.com/cse?cx=004341253442084066054:hqcqt8c54li")
    text_area= driver.find_element_by_id("gsc-i-id1")
    text_area.send_keys(x+ "\n")

    #print("waiting for shit to load")
    time.sleep(2)
    #grabs raw html
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    def grabbing(soup, x):
        #grabs content puts it in a dict
        master_dict=[]
        #holds transfer topic to local val for later storage in dict
        trend=x
        
        print("grabbing some soup")
        
        for y in soup.find_all('div', class_="gs-webResult gs-result")[:10]:
            title = y.find('a',class_="gs-title").text.strip()
            #link = y.find('div', class_="gs-bidi-start-align gs-visibleUrl gs-visibleUrl-long").text.strip()
            link = y.find('a', class_="gs-title")["href"]
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
                    
            temp_dict = {'Title':title, 'Trend':trend,'URL':link, 'post_date':article_date,'Thumbnail':art}
            master_dict.append(temp_dict)
            
        return master_dict
    #Keeps the dict updated with info from new topic
    print("Dict updated")
    master_dict= master_dict + grabbing(soup,x)
driver.quit()
print("killed chrome sucessfull")
df = pd.DataFrame.from_dict(master_dict)
#clears dict in case of overlapping data
df.to_csv('query_export.csv', encoding='utf-8')

print('an export has been created')
print(df)
#clears dict in case of overlapping data
master_dict=[]


# In[ ]:




