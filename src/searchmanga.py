from bs4 import BeautifulSoup as bs     # The source code parser
import requests                         # Library to make HTTP requests
from request import send_request
from settings import SEARCH 

def find_manga_pages_links(seriesName):
    
    search_url      = SEARCH + seriesName
    raw_html        = send_request(search_url).text

    # Scrap the html to find the manga page link
    parsed_html     = bs(raw_html, "html.parser")

    return parsed_html.find_all("a", {"class": "item-img"})

def find_chapter_link(mangaPageLink):
    raw_html        = send_request(mangaPageLink).text

    # Scrap the html to find the chapter link
    parsed_html     = bs(raw_html, "html.parser")

    return parsed_html.find("img", {"id": "img"}).get("src")


def list_of_search_results(mangaName):
    manga_pages_links = find_manga_pages_links(mangaName) 
    lista_resultados = []

    for x in range(len(manga_pages_links)):                  
        lista_resultados.append(manga_pages_links[x].get("href"))
    return lista_resultados

#print(list_of_search_results("naruto"))