import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.scrapethissite.com/pages/simple/"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
les_pays=[]
liste_pays=soup.find_all(class_='col-md-4 country')

en_tete = ["pays", "capitale"]
with open('data_exo2.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    for pays in (liste_pays):
        ligne = [pays.find(class_='country-name').get_text(strip=True), pays.find(class_='country-capital').get_text(strip=True)]
        writer.writerow(ligne)