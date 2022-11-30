import requests
from bs4 import BeautifulSoup

class Extract():

    def get_deets(self, name):

        req = requests.get(f'https://github.com/{name}')

        soup = BeautifulSoup(req.content, 'lxml')

        dlist = [] 

        pic = soup.find('img', class_ = 'avatar avatar-user width-full border color-bg-default')['src']
        repo = soup.find('span', class_ ='Counter').text

        
        profile = {
            'Name' : name,
            'Picture' : pic,
            'Number of repos' : repo
        }
        dlist.append(profile)
        

        return dlist


