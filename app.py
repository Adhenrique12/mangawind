import os
import requests
from bs4 import BeautifulSoup
from progress.bar import Bar
import shutil
from search_manga import chosen_manga


link_anime = chosen_manga()

#Selecionar capitulo 
numero_capitulo = input('Entre com o entervalo dos capitulos separado com  -   :  ')
comeco_capitulo = -1 * int(numero_capitulo[0])
fim_capitulo = -1 * int(numero_capitulo[2::])


#Iniciar url e fazer soup
manga = requests.get(link_anime)
soup = BeautifulSoup(manga.text,'lxml')

#Apanhar o nome do manga a ser baixado
nome_anime = soup.body.h1.find_all(string=True) #Apanhar nome anime
print(str(nome_anime[0]))

#Apanhar os links dos capitulos
cap_manga = soup.find(class_= "chapter-list")
capituloss = cap_manga.find_all('a') #Div Link dos capitulos


capitulos_link = [] #todos os links dos capitulos

for capitulos in capituloss:
    capitulos_link.append(str(capitulos.attrs['href'])) 

capitulos_link = capitulos_link[::-1]
#Baixando as imagens dos capitulos


bar1 = Bar('Baixando', max = len(capitulos_link))
count = 0
for capitulo_link in capitulos_link:
    count += 1
    capitulo_links = requests.get(capitulo_link)
    soup_capitulo = BeautifulSoup(capitulo_links.text,'lxml')

    #Encontrar as imagens
    class_imagem = soup_capitulo.find(class_= "vung-doc")
    tag_imagem = class_imagem.find_all('img')
    imagens = [] #Lista de todas as imagens do capitulo
    for img in tag_imagem:
        imagens.append(str(img.attrs['src'])) 

    #Baixando imagem
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


    

      








