from bs4 import BeautifulSoup as bs

def search_manga(manga: str):
    """
    Constructs the search query URL
    """
    query_url = 'https://manganelo.com/search/story/'
    manga = "_".join(manga.split(" ")).lower()
    return query_url + manga

def search_results(search_query_html: str):
    """
    Takes a search query and returns search result of the manga.
    It returns a dictionary with all the results and their links.
    """
    manga_links = search_query_html.select('div.search-story-item div.item-right a.item-title')
    results = []

    for link in range(len(manga_links)):                  
        results.append(dict(url=manga_links[link].get("href"), name=manga_links[link].get("title")))
    return results
    
def manga_chapters(manga_page_html: str):
    """
    Returns dictionary with chapter and links
    """
    chapter_links = manga_page_html.select('div.panel-story-chapter-list a.chapter-name.text-nowrap')
    results = []
    for link in range(len(chapter_links)):                  
        results.append(dict(url=chapter_links[link].get("href"), chapter=chapter_links[link].get("title")))
    return results


def get_chapter_page(chosen_chapter_url: int, single_page=True, page_number=1):
    """
    Returns the page with the images to be scraped by MangaWind.
    if single_page = False it uses the page_number variable to loop
    through the pages of the chapter that was chosen.
    """
    if single_page:
        image_tags = chosen_chapter_url.select('div.container-chapter-reader img')
        images = []
        for image in image_tags:
            images.append(image.get('src'))
        return images
    else:
        pass