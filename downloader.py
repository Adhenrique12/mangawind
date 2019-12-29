import os
import requests
from bs4 import BeautifulSoup # type: ignore
from progress.bar import Bar # type: ignore
import shutil
import app as main

class MangaFinder:
    def __init__(self, manga_link: str, number_of_chapters: list):
        self.manga_link = manga_link
        self.first_chapter = int(number_of_chapters[0])
        if len(number_of_chapters) == 1:
            self.last_chapter = self.first_chapter
        else:
            self.last_chapter = int(number_of_chapters[1])

    @property
    def soup(self):
        return BeautifulSoup(requests.get(self.manga_link).text,'lxml')

    @property
    def manga_name(self):
        return self.soup.body.h1.find_all(string=True)

    @property
    def manga_chapter(self):
        if self.soup.find(class_="chapter-list") == None:
            return self.soup.find(class_="row-content-chapter").find_all('a')
        return self.soup.find(class_="chapter-list").find_all('a')

    @property
    def chapters_link(self):
        self.link: list = []
        for manga_chapter in self.manga_chapter:
            self.link.append(str(manga_chapter.attrs['href']))
        return  self.link[::-1]

    @property
    def chosen_chapters(self):
        if self.manga_chapter[self.last_chapter] == self.manga_chapter[-1]:
            return self.chapters_link[self.first_chapter:]
        else:
            return self.chapters_link[self.first_chapter - 1:self.last_chapter + 1] 

class Downloader:
    def __init__(self,chapter_link, manga_name):
        self.chapter_link = chapter_link
        self.chapter_number = chapter_link.split('/')[-1].split('_')[-1]
        self.manga_name = manga_name[0]
    @property
    def images(self):
        if self.soup.find(class_="vung-doc")  == None:
            image_tag: list = self.soup.find(class_="container-chapter-reader").find_all('img')
        else:
            image_tag: list = self.soup.find(class_="vung-doc").find_all('img')
        images: list = [] #The list of all images in the chapter
        for img in image_tag:
            images.append(str(img.attrs['src'])) 
        return images

    @property
    def soup(self):
        return BeautifulSoup(requests.get(self.chapter_link).text,'lxml')

    @property
    def newpath(self):
        return str(self.manga_name) + '_' + str(self.chapter_number) + '/'

    def makedir(self):
        try:
            os.makedirs(self.newpath)
        except:
            print('This chapter already exists.')
            exit()
    
    def downloaded_image(self, episode_number):
        bar = Bar(f'Downloading episode {episode_number}', max=len(self.images))
        counter: int = 0
        for image in self.images:
            counter += 1
            number = str(counter)
            full_path = self.newpath + number + '.jpg'
            response = requests.get(image, stream=True)
            with open(full_path, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
            del response
            bar.next()
        bar.finish()

# Download the chapters' images
def run(chapter_interval: str, pdf_only: bool):
    app = MangaFinder(main.manga.run(), chapter_interval)
    for chapter_link in app.chosen_chapters:
        manga = Downloader(chapter_link, app.manga_name)
        manga.makedir()
        manga.downloaded_image(manga.chapter_number)
        os.chdir(manga.newpath)

        chapter = app.manga_name[0] + '_' + str(manga.chapter_number)
        if pdf_only:
            main.manga.convert_to_pdf(chapter)
            shutil.move(chapter + '.pdf', '..')
            os.chdir('..')
            shutil.rmtree(chapter + '/')
        else:
            os.chdir('..')