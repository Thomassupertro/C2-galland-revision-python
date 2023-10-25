import requests
from bs4 import BeautifulSoup
import csv
en_tete= ["Equipe bon ratio"]
with open('data_exo4.csv', 'w') as fichier_csv:
    writer = csv.writer(fichier_csv, delimiter=",")
    writer.writerow(en_tete)
    for i in range(1,2):
        url = "https://www.scrapethissite.com/pages/forms/?page_num="+str(i)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        en_tete= ["Equipe", "année","pourcentage"]
        liste_teams=soup.find_all(class_='team')
        for team in (liste_teams):
            if(team.find(class_="wins").get_text(strip=True)>team.find(class_="losses").get_text(strip=True)):
                writer.writerow([team.get_text(strip=True)])

