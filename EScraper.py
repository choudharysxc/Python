import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

lst=list()
final_lst=list()

def Convert(x):
    link=urllib.request.urlopen(x)
    soup=BeautifulSoup(link,'html.parser')
    return soup

def scraper(url):
    
    y=Convert(url)
    num=0

    for links in y.findAll('a'):
        lst.append(links.get('href'))
    
    
    for i in lst:
        j=i
        i=str(i)
        num=i.find('@')
        if num > 1  :
                final_lst.append(j)
    for g in final_lst:
        print(g)

        #scraper(links)
    

url=input("Enter the Url :")
scraper(url)


