import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops" 
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html5lib') 
   
infos=[]  # a list to store quotes 
   
product = soup.find('div', attrs = {'class':'col-lg-9'})  
   
for row in product.findAll('div', 
                         attrs = {'class':'caption'}): 
    info = {} 
    info['price'] = row.h4.text 
    info['title'] = row.a['title'] 
    info['desc'] = row.find('p').getText()
    infos.append(info) 
   
filename = 'webscrap_output_singlepage.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['price','title','desc']) 
    w.writeheader() 
    for info in infos: 
        w.writerow(info) 