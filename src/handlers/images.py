from request_h import send_request
from progress.bar import Bar
import shutil
import os


def download_images(chapter_imgs: list, manga_name: str):
    os.makedirs(f'./{manga_name}')
    number = 0
    for image_url in chapter_imgs:
        number += 1
        image = send_request(image_url, binary=True)
        with open(f'./{manga_name}/{number}.jpg' ,'wb') as file:
            shutil.copyfileobj(image.raw, file)

lista = ['https://s3.mkklcdnv3.com/mangakakalot/r1/read_naruto_manga_online_free3/vol72_chapter_6991_the_seal_of_reconciliation/1.jpg']
download_images(lista, 'naruto')