from PIL import Image
import os
def convert_to_pdf():
    manga_folder = sorted(os.listdir())
    first_chapter = Image.open(manga_folder[0])
    chapters = []
    for chapter in manga_folder:
        if chapter == first_chapter:
            continue
        chapters.append(Image.open(chapter))
    first_chapter.save('chapter.pdf', save_all=True, append_images=chapters[1::])

def handle_dir(current_dir: str):
    pass
