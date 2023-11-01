import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup
import tkinter
from tkinter import messagebox

url='https://www.timeanddate.com/weather/india/kolkata'  #website to fetch data from

http=urllib.request.urlopen(url)   #getting url data
soup=BeautifulSoup(http,'html.parser')  #converting into soup (not caring about the format)

y=soup.find(id="qlook")  
y=y.find_all("div")
y=str(y)

y=y.split(',')
y=y[1]
num1=y.find('>')
num2=y.find('C')
y=y[num1+1:num2+1]

root=tkinter.Tk()   #making root tkinter obj
root.geometry('500x200')

messagebox.showinfo("The Weather is ","Weather in kolkata is :" + y) #shows the info 



