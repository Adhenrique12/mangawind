from bs4 import BeautifulSoup # type: ignore
import requests as r
from PIL import Image # type: ignore
from typing import List
import os

website: str = "https://mangakakalot.com/"
manga: str = input("What manga do you want to search for? ")
def chosen_manga() -> str:
    def search_result(manga: str=manga) -> str:
        manga = manga.replace(' ', '_')
        search = r.post(website + 'search/' + manga)
        # Return the search result as html
        return search.text

    def manga_choice() -> List[int]:
        print('These are the results: \n')
        choices: list = []
        counter: int = 0
        totalnum_chapters: list = soup.find_all('em', class_='story_chapter')
        for link in soup.find_all('h3', class_='story_name'):
            counter += 1
            choices.append(link.a['href'])
            # Print a numbered list of the search result
            print(counter, link.a.text + ' >> Last chapter: ' + str(totalnum_chapters[counter].text.strip()))
        # Return the list of links from the search result
        return choices

    def choose_manga(manga_links: list) -> str:
        choices: list = manga_links
        choice: int = int(input("Type the number of the manga of your choice "))
        return choices[choice - 1]

    soup = BeautifulSoup(search_result(), 'lxml')
    return choose_manga(manga_choice())

def convert_to_pdf(chapter_name: str="chapter"):
    manga_folder: list = os.listdir()
    first_chapter = Image.open(manga_folder[0])
    chapters: list = []
    for chapter in manga_folder:
        chapters.append(Image.open(chapter))
    first_chapter.save(chapter_name + '.pdf', save_all=True, append_images=chapters[1::])