import requests
from bs4 import BeautifulSoup
import smtplib

class Scraper:
    def __init__(self, keywords:list, articles:int):
        self.url = 'https://news.ycombinator.com/news?p='
        self.page = 1
        self.update()
        self.articles = articles
        self.keywords = keywords
        self.links_liked = {}
        self.message = ''

    
    def parse(self):
        data = BeautifulSoup(self.response, 'html.parser')
        links = data.find_all('a', class_='titlelink')
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.links_liked[link.text] = link['href']


        if len(self.links_liked) >= self.articles:
            return 
        else:
            if self.page >= 100:
                print('Could not find all things you wanted :(')
            if self.page < 100:
                self.page += 1
                self.update()
                self.parse()


    def update(self):
        self.new_url = self.url + str(self.page)
        self.response = requests.get(self.new_url).text

    def get_data(self):
        return self.links_liked



subjects = input("Please type subjects you want to search for. seperated by ';'\nExample: 'internet;tech;economy'\n>")
news_length = input('How many news you wanna Find? ')
s = Scraper(subjects.split(';'), int(news_length))
s.parse()
data = s.get_data()
print(data)