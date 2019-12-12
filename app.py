import os
import requests
from bs4 import BeautifulSoup # type: ignore
from progress.bar import Bar # type: ignore
import shutil
from MangaManipulation import MangaManipulation 

class App:

    def __init__(self, link_anime: str, number_of_chapters: list):
        self.link_anime = link_anime
        self.first_chapter = int(number_of_chapters[0]) - 1
        if len(number_of_chapters) == 1:
            self.last_chapter = self.first_chapter
        else:
            self.last_chapter = int(number_of_chapters[1])

   


    @property
    def soup(self):
        return BeautifulSoup(requests.get(self.link_anime).text,'lxml')
    @property
    def manga_name(self):
        return self.soup.body.h1.find_all(string=True)

    @property
    def manga_chapter(self):
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
            return self.chapters_link[self.first_chapter:self.last_chapter + 1] 







# Take the name of the manga that should be downloaded and the interval
app = App(MangaManipulation().run(),input('Enter a chapter interval separated by hifens: ').split('-',1))

# Download the chapters' images
for chapter_link in app.chosen_chapters:
    
    current_chapter_link = requests.get(chapter_link)
    chapter_soup = BeautifulSoup(current_chapter_link.text,'lxml')

    #Find the Chapter number
    chapter_number: int = chapter_link.split('/')[-1].split('_')[-1]
    
    # Find the images
    image_class = chapter_soup.find(class_="vung-doc")
    image_tag: list = image_class.find_all('img')
    images: list = [] # The list of all images in the chapter
    for img in image_tag:
        images.append(str(img.attrs['src'])) 

    # Downloading images
    newpath: str = str(app.manga_name[0]) + '_' + str(chapter_number) + '/'
    try:
        os.makedirs(newpath)
    except:
        print('This chapter already exists.')
        break

    bar = Bar('Downloading', max=len(images))
    counter: int = 0
    for image in images:
        counter += 1
        number = str(counter)
        full_path = newpath + number + '.jpg'
        response = requests.get(image, stream=True)
        with open(full_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        bar.next()
    os.chdir(newpath)
    MangaManipulation.convert_to_pdf(str(app.manga_name[0]) + '_' + str(chapter_number))
    os.chdir('..')
    bar.finish()