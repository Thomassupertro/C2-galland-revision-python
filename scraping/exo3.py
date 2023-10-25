import requests
from bs4 import BeautifulSoup
import csv
en_tete= ["Equipe", "année","pourcentage"]
with open('data_exo3.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=',')
    writer.writerow(en_tete)
    for i in range(1,4):
        url = "https://www.scrapethissite.com/pages/forms/?page_num="+str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        en_tete= ["Equipe", "année","pourcentage"]
        liste_teams=soup.find_all(class_='team')
        for team in (liste_teams):
            ligne = [team.find(class_='name').get_text(strip=True), team.find(class_='year').get_text(strip=True), team.find(class_='pct').get_text(strip=True)]
            writer.writerow(ligne)

