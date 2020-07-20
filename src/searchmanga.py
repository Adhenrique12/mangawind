from bs4 import BeautifulSoup as bs     # The source code parser
import requests                         # Library to make HTTP requests
from request import send_request
from settings import SEARCH 

def find_manga_pages_links(seriesName):
    
    search_url = SEARCH + seriesName
    raw_html       = send_request(search_url).text
    # Scrap the html to find the manga page link
    parsed_html = bs(raw_html, "html.parser")

    return parsed_html.find_all("a", {"class": "item-img"})



manga_pages_links = find_manga_pages_links("dragon_ball") #exemplo mudar

for x in range(len(manga_pages_links)):                  
    print(manga_pages_links[x].get("href"))


