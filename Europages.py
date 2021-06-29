import requests
from bs4 import BeautifulSoup
import sqlite3

conn1 = sqlite3.connect('Europages.db')
c= conn1.cursor()
c.execute('''CREATE TABLE Companies (Company Name TEXT, Logo TEXT , Descriptiom TEXT, Website TEXT)''')

class Europage:
    def fetch(self ,i):
        if i==1:
            url= f'https://www.europages.co.uk/companies/transport.html'
        else :
            url=f"https://www.europages.co.uk/companies/pg-"+str(i)+"/transport.html"
        res= requests.get(url)
        self.soup= BeautifulSoup(res.text , 'lxml')

    def scrape(self):
        self.rows= self.soup.find_all('li' , class_="article-company card card--1dp vcard")
    
    def descrifuncc(self):
        try:

            website = requests.get(self.link)
            soup1 = BeautifulSoup(website.text ,"lxml")
            descrip = soup1.find('p' , class_="company-description").text
        except Exception:
            descrip="NULL"
        return descrip

    def element(self):
       for self.row in self.rows:
            mylist=[]
            try:
                self.name=self.row.find('div' , class_="company-info").a.text.replace('\n' ,'').replace('\r' , '').replace('\t' , '')
            except Exception:
                self.name = "NULL"
            try:
                self.logo = self.row.find('div' , class_="company-logo u-clickable js-ecard-delegate").img["src"]
            except Exception:
                self.logo="NULL"
            try:
                self.website = self.row.find('div' , class_="company-website").a["href"]
            except Exception:
                self.website="NULL"
            try:
                self.link=self.row.find('div' , class_="company-info").a["href"]
            except Exception:
                self.link="NULL"
            self.description=self.descrifuncc()

            c.execute('''INSERT INTO Companies VALUES(?,?,?,?)''', (self.name ,self.logo,self.description,self.website))

    def run(self):
        for i in range (1,19):
            self.fetch(i)
            self.scrape()
            self.element()


if __name__ == "__main__":
    x=Europage()
    x.run()

conn1.commit()
#print('complete')
#c.execute('''SELECT * FROM Companies''')
#r=c.fetchall()



        
                

    
    
        
