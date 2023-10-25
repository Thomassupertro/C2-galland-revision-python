import requests
from bs4 import BeautifulSoup
url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
les_pays=[]
liste_pays=soup.find_all(class_='country-name')
for pays in liste_pays:
    print(pays.get_text(strip=True))
