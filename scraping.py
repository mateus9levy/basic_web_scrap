from pathlib import Path
import requests
from bs4 import BeautifulSoup
import json
import re

def setNumberOfPages():
    nPages = int(input("Insert number of pages to be scraped:\n"))
    return nPages

def getImage(html):
    html = f'{html}'
    hrefPattern = r'href="([^"]*)"'
    srcPattern = r'src="([^"]*)"'
    match = re.search(hrefPattern, html)
    if match:   
        href = match.group(1)
        request = requests.get(f'https://opencritic.com{href}')
        soup = BeautifulSoup(request.text, "html.parser")
        image = soup.find_all("div",attrs={"class":"header-image-container"})
        if(image == []):
            return False
        else:
            matchSrc = re.search(srcPattern,f'{image[0]}')
            src = matchSrc.group(1)
            return src

def scrapGamePages():
    games = []
    maxPages = setNumberOfPages()
    for i in range(1,maxPages+1):
        print(f'Scraping page {i}...')
        request = requests.get(f'https://opencritic.com/browse/all/all-time/name?page={i}')
        soup = BeautifulSoup(request.text,"html.parser")
        dates = soup.find_all("div",attrs={"class":"first-release-date col-auto show-year"})
        gameNames = soup.find_all("div",attrs={"class":"game-name col"})
        rating = soup.find_all("div",attrs={"class": "score col-auto"})
        plataforms = soup.find_all("div",attrs={"class": "platforms col-auto"})
        for j in range (0,len(rating)):
            rate = rating[j].text
            a_tag = gameNames[j].find('a')
            gameName = a_tag.text
            gameLink = a_tag  
            imageSrc = getImage(gameLink)
            if(rate != " " and imageSrc != False):
                date = dates[j].find('span')
                date = date.text
                plataform = plataforms[j].text
                rate = rate [:-1]
                rate = rate [1:] 
                plataform = plataform [:-1]
                plataform = plataform [1:]
                games.append({
                    "name": gameName,
                    "rating": rate,
                    "plataforms": plataform,
                    "date": date,
                    "image": imageSrc
                })

    print("Scraping fineshed!")
    return games


def printJson(game):
    with open('data.json', "w") as arquivo:
        arquivo.write("[")
        for item in game:
            json.dump(item,arquivo,ensure_ascii=False)
            arquivo.write(",\n")
        arquivo.write("]")


games = scrapGamePages()
printJson(games)
