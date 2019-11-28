import os
import requests
from bs4 import BeautifulSoup
from progress.bar import Bar
import shutil
from search_manga import chosen_manga

link_anime = chosen_manga()

#Choose chapters
numero_capitulo = input('Entre com o entervalo dos capitulos separado com  -  s:  ')
numero_capitulo = numero_capitulo.split('-',1)
comeco_capitulo = int(numero_capitulo[0])
fimcapitulo = int(numero_capitulo[1])

# Initialize url and make a soup
manga = requests.get(link_anime)
soup = BeautifulSoup(manga.text,'lxml')

# Take the name of the manga that should be downloaded
nome_anime = soup.body.h1.find_all(string=True) #Apanhar nome anime
print(str(nome_anime[0]))

# Take the chapter links
cap_manga = soup.find(class_= "chapter-list")
capituloss = cap_manga.find_all('a') #Div Link dos capitulos

capitulos_link = [] # The link of all chapters

for capitulos in capituloss:
    capitulos_link.append(str(capitulos.attrs['href'])) 

capitulos_link = capitulos_link[::-1]

# Select range to download chapter
chapter_chose = []
chapter_chose = capitulos_link[comeco_capitulo:fimcapitulo]

# Download the chapters' images
bar1 = Bar('Baixando', max = len(chapter_chose))
count = 0
for capitulo_link in chapter_chose:
    count += 1
    capitulo_links = requests.get(capitulo_link)
    soup_capitulo = BeautifulSoup(capitulo_links.text,'lxml')

    # Find the images
    class_imagem = soup_capitulo.find(class_= "vung-doc")
    tag_imagem = class_imagem.find_all('img')
    imagens = [] # The list of all images in the chapter
    for img in tag_imagem:
        imagens.append(str(img.attrs['src'])) 

    # Downloading images
    newpath = str(nome_anime[0]) + str(count) + '/'
    os.makedirs(newpath)

    bar = Bar('Baixando', max = len(imagens))
    contar_numero = 0
    for imagem in imagens:
        contar_numero += 1
        numero = str(contar_numero)
        full_path = newpath + str(nome_anime[0]) + numero + '.jpg'
        response = requests.get(imagem, stream=True)
        with open(full_path, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        bar.next()
    bar.finish()
    bar1.next()
bar1.finish()