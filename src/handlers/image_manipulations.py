from request_h import send_request
from progress.bar import Bar
import shutil
import os


def download_images(chapter_imgs: list, chapter_name: str):
    '''
    Takes a list of image urls and the name of the chapter to download
    '''
    try:
        os.makedirs(f'./{chapter_name}')
    except FileExistsError:
        pass

    number = 0
    bar = Bar(f'Downloading {chapter_name}', max=len(chapter_imgs))
    for image_url in chapter_imgs:
        number += 1
        image = send_request(image_url, binary=True)
        with open(f'./{chapter_name}/{number}.jpg' ,'wb') as file:
            shutil.copyfileobj(image.raw, file)
        bar.next()  
    bar.finish()