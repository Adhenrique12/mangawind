import os
import requests
from bs4 import BeautifulSoup
from progress.bar import Bar
import shutil
from search_manga import chosen_manga

link_anime = chosen_manga()

#Choose chapters
number_of_chapters = input('Enter a chapter interval separated by hifens: ')
number_of_chapters = number_of_chapters.split('-',1)
first_chapter = int(number_of_chapters[0])
last_chapter = int(number_of_chapters[1])

# Initialize url and make a soup
manga = requests.get(link_anime)
soup = BeautifulSoup(manga.text,'lxml')

# Take the name of the manga that should be downloaded
manga_name = soup.body.h1.find_all(string=True) #Apanhar nome anime

# Take the chapter links
manga_chapter = soup.find(class_="chapter-list")
chapters = manga_chapter.find_all('a') #Div link of all manga chapters

chapters_link = [] # The link of all chapters

for manga_chapters in chapters:
    chapters_link.append(str(manga_chapters.attrs['href'])) 

chapters_link = chapters_link[::-1]

# Select range to download chapter
chosen_chapters = []

if chapters[last_chapter] == chapters[-1]:
    chosen_chapters = chapters_link[first_chapter:]
else:
    chosen_chapters = chapters_link[first_chapter:last_chapter + 1]

# Download the chapters' images
bar1 = Bar('Downloading', max = len(chosen_chapters))
count = 0
for chapter_link in chosen_chapters:
    count += 1
    current_chapter_link = requests.get(chapter_link)
    chapter_soup = BeautifulSoup(current_chapter_link.text,'lxml')

    # Find the images
    image_class = chapter_soup.find(class_="vung-doc")
    image_tag = image_class.find_all('img')
    images = [] # The list of all images in the chapter
    for img in image_tag:
        images.append(str(img.attrs['src'])) 

    # Downloading images
    newpath = str(manga_name[0]) + str(count) + '/'
    os.makedirs(newpath)

    bar = Bar('Downloading', max=len(images))
    counter = 0
    for image in images:
        counter += 1
        number = str(counter)
        full_path = newpath + str(manga_name[0]) + number + '.jpg'
        response = requests.get(image, stream=True)
        with open(full_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        bar.next()
    bar.finish()
    bar1.next()
bar1.finish()