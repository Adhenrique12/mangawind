from bs4 import BeautifulSoup # type: ignore
import requests as r
from PIL import Image # type: ignore
from typing import List
import os

class MangaManipulation:
    def __init__(self, manga, choice):
        self.website: str = "https://mangakakalot.com/"
        self.manga = manga
        self.choice = choice

    @property
    def soup(self):
        return BeautifulSoup(self.search_result(self.manga), 'lxml')
    
    def search_result(self, manga: str) -> str:
        manga = manga.replace(' ', '_')
        search = r.post(self.website + 'search/' + manga)
        # Return the search result as html
        return search.text

    def manga_choice(self) -> List[int]:
        soup = self.soup
        choices: list = []
        counter: int = 0
        totalnum_chapters: list = soup.find_all('em', class_='story_chapter')
        if self.choice is None:
            print("Here's what we found:\n")
        for link in soup.find_all('h3', class_='story_name'):
            counter += 1
            choices.append(link.a['href'])
            # Print a numbered list of the search result
            if self.choice is None:
                print(counter, link.a.text + ' >> Last chapter: ' + str(totalnum_chapters[counter].text.strip()))
        # Return the list of links from the search result
        return choices
    
    def choose_manga(self, manga_links: list) -> str:
        choices: list = manga_links
        return choices[self.choice - 1]

    def run(self):
        if self.choice is not None:
            return self.choose_manga(self.manga_choice())
        else:
            return self.manga_choice()

    @staticmethod
    def convert_to_pdf(chapter_name: str="chapter"):
        manga_folder: list = os.listdir()
        first_chapter = Image.open('1.jpg')
        count = 2
        chapters= []
        chapters.append(Image.open('2.jpg'))
        while count != len(manga_folder) + 1:
            chapters.append(Image.open(str(count) + '.jpg'))
            count += 1
        
        first_chapter.save(chapter_name + '.pdf', save_all=True, append_images=chapters[1::])