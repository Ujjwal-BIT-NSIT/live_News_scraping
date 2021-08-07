from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
i=0
def call_page(i):
    if i ==0:
        html_text= requests.get('https://www.ndtv.com/world-news')
    else:
        html_text= requests.get('https://www.ndtv.com/world-news/page-' + str(i))
    soup=BeautifulSoup(html_text.text,'html.parser')
    news=soup.find_all('div',class_='news_Itm-cont')
    df = pd.read_csv('C:\\Users\\hp\\Desktop\\web scraping\\news93045100685596.csv')
    # df = pd.read_csv('C:\\Users\\hp\\Downloads\\newsss smn.csv')
    with open ('news93045100685596.csv','w',newline='') as file:
        csv_writer = csv.writer(file, delimiter=',' ) 
        w=0  
        for n in news:
            comp3=n.find('a').get('href')
            if df.iloc[0,4] == comp3:
            # if df.link[0] == comp3:
                print('no. of new news is', w )
                exit()
            tags1 =n.find('h2', class_='newsHdng').text
            print(tags1)
            comp=n.find('span', class_='posted-by').text.split()[0]
            print(comp) #Telling us the source of the news
            comp2=n.find('span', class_='posted-by').text.split()[2:6]   
            print(comp2) #Tells us the published date
            comp5=n.find('span', class_='posted-by').text.split()[6:10]
            print(comp5) #Tells us the city 
            comp3=n.find('a').get('href')
            print (comp3)# Tells us the link of the news
            data = [tags1,comp,comp2,comp5,comp3]
            csv_writer.writerow(data)
            w=w+1
x=0        
for x in range(15):
    call_page(x)    