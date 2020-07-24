from request_h import send_request
from progress.bar import Bar
import shutil
import os


def download_images(chapter_imgs: list, chapter_name: str):
    try:
        os.makedirs(f'./{chapter_name}')
    except FileExistsError:
        pass

    number = 0
    bar = Bar(f'Downloading chapter {chapter_name}', max=len(chapter_imgs))
    for image_url in chapter_imgs:
        number += 1
        image = send_request(image_url, binary=True)
        with open(f'./{chapter_name}/{number}.jpg' ,'wb') as file:
            shutil.copyfileobj(image.raw, file)
        bar.next()  
    bar.finish()

lista = ['https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.XmpsNQ0ZvIsPBPGD3DyfKwHaEK%26pid%3DApi&f=1', 'https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.XmpsNQ0ZvIsPBPGD3DyfKwHaEK%26pid%3DApi&f=1']
download_images(lista, 'naruto')