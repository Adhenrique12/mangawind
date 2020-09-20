from bs4 import BeautifulSoup as bs
from scrapers.scraper import Scrapers
from handlers import request_h
from handlers.image_manipulations import download_images

def soup(search_url: str): 
       raw_html = request_h.send_request(search_url).text # Scrape the html to find the chapter link
       return bs(raw_html, "lxml")

def main():
    new_class = Scrapers()
    link = soup('https://manganelo.com/chapter/read_naruto_manga_online_free3/chapter_699.1')
    download_images(new_class.get_chapter_page(link), 'naruto')
    print(new_class.get_chapter_page(link))

if __name__ == '__main__':
    main()
