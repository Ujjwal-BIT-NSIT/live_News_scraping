from ntpath import join
from bs4 import BeautifulSoup
import csv
import requests
import pandas as pd
import os
path = os.getcwd()
folder_path = os.path.join(path + "/" + "ndtv")
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    file_path = os.path.join(folder_path + "/" + "newscraper.csv")
else:
    
    file_path = os.path.join(folder_path + "/" + "newscraper.csv")
    pass
g = input("Are you running this code for the first time y/n ?")
if g == 'y' or g == 'Y':
    with open(file_path, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        field = ["Headlines", "Source", "Time", "Place", "Url", "id-generated"]
        csv_writer.writerow(field)

if g== 'n' or g=='N':
    df = pd.read_csv(file_path)
    df = df.loc[::-1]
    df.to_csv(file_path, index=False)

new_news=[]

def superpower(n):
    with open(file_path, 'a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        tags1 = n.find('h2', class_='newsHdng').text
        comp = n.find('span', class_='posted-by').text.split()[0]
        comp2 = n.find('span', class_='posted-by').text.split()[2:6]
        comp5 = n.find('span', class_='posted-by').text.split()[6:10]
        comp3 = n.find('a').get('href')
        comp4 = n.find('a').get('href').split('-')[-1]
        data = [tags1, comp, comp2, comp5, comp3, comp4]
        csv_writer.writerow(data)

def call_page(i):
    html_text = requests.get('https://www.ndtv.com/world-news/page-' + str(i))
    soup = BeautifulSoup(html_text.text, 'html.parser')
    news = soup.find_all('div', class_='news_Itm-cont')
    for w in news:
        if g == 'n' or g == 'N':
            comp3 = w.find('a').get('href')
            df = pd.read_csv(file_path)
            if comp3 in df.values:
                latest_news()
                df = pd.read_csv(file_path)
                df = df.loc[::-1]
                df.to_csv(file_path, index=False)
                exit()

            else:
                new_news.append(w)
        else:
            
            superpower(w)
def latest_news():
    k=1
    for nw in reversed(new_news):
        superpower(nw)
        k=k+1

z = 1
for x in range(z, 15):
    call_page(x)


