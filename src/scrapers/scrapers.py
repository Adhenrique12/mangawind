from bs4 import BeautifulSoup as bs
import yaml

SERVER_CONFIG_FILE = 'manganelo.yml'


try:
    with open(SEVER_CONFIG_FILE, 'r') as file:
        conf = yaml.safe_load(file)
except FileNotFoundError:
    print("No configuration file was found")


def search_manga(manga: str):
    """
    Constructs the search query URL
    """
    query_url = conf.SERVER_LINK_SEARCH
    manga = conf.SERVER_LINK_SEARCH_SPLIT.join(manga.split(" ")).lower()
    return query_url + manga

def search_results(search_query_html: str):
    """
    Takes a search query and returns search result of the manga.
    It returns a dictionary with all the results and their links.
    """
    manga_links = search_query_html.select(conf.SERVER_LINK_SEARCH_TAG)
    results = []

    for link in range(len(manga_links)):
        results.append(dict(url=manga_links[link].get("href"), name=manga_links[link].get("title")))
    return results

def manga_chapters(manga_page_html: str):
    """
    Returns dictionary with chapter and links
    """
    chapter_links = manga_page_html.select(conf.SERVER_CHAPTERS_TAG)
    results = []
    for link in range(len(chapter_links)):
        results.append(dict(url=chapter_links[link].get("href"), chapter=chapter_links[link].get("title")))
    return results


def get_chapter_page(chosen_chapter_url: int, single_page=SINGLE_PAGE_READER, page_number=1):
    """
    Returns the page with the images to be scraped by MangaWind.
    if single_page = False it uses the page_number variable to loop
    through the pages of the chapter that was chosen.
    """
    if single_page:
        image_tags = chosen_chapter_url.select(conf.SERVER_IMG_TAG)
        images = []
        for image in image_tags:
            images.append(image.get('src'))
        return images
    else:
        pass
