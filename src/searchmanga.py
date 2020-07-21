from bs4 import BeautifulSoup as bs     # The source code parser
import requests                         # Library to make HTTP requests
from request import send_request
from settings import SEARCH 

def soup(search_url):
    raw_html        = send_request(search_url).text

    # Scrap the html to find the chapter link
    return bs(raw_html, "html.parser")


def find_manga_pages_links(seriesName):
    
    search_url      = SEARCH + seriesName

    return soup(search_url).find_all("a", {"class": "item-img"})


def list_of_search_results(mangaName):
    manga_pages_links = find_manga_pages_links(mangaName) 
    lista_resultados = []

    for x in range(len(manga_pages_links)):                  
        lista_resultados.append(manga_pages_links[x].get("href"))
    return lista_resultados


def list_of_all_chapters(url):

    lista_chapters_raw = soup(url).find_all("a", {"class" : "chapter-name text-nowrap"}, "href")
    lista_chapters = []

    for x in range(len(lista_chapters_raw)):                  
        lista_chapters.append(lista_chapters_raw[x].attrs['href'])
    
    return lista_chapters




