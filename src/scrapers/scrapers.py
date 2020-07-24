from bs4 import BeautifulSoup as bs
import yaml



class Scrapers:

    def __init__(self):
        SERVER_CONFIG_FILE = 'scrapers/manganelo.yml'
        try:
            with open(SERVER_CONFIG_FILE, 'r') as file:
                self.conf = yaml.safe_load(file)
        except FileNotFoundError:
            print("No configuration file was found")

    def search_manga(self, manga: str):
        """
        Constructs the search query URL
        """
        query_url = self.conf['SERVER_LINK_SEARCH']
        manga = self.conf['SERVER_LINK_SEARCH_SPLIT'].join(manga.split(" ")).lower()
        return query_url + manga

    def search_results(self, search_query_html: str):
        """
        Takes a search query and returns search result of the manga.
        It returns a dictionary with all the results and their links.
        """
        manga_links = search_query_html.select(self.conf['SERVER_LINK_SEARCH_TAG'])
        results = []

        for link in range(len(manga_links)):
            results.append(dict(url=manga_links[link].get("href"), name=manga_links[link].get("title")))
        return results

    def manga_chapters(self, manga_page_html: str):
        """
        Returns dictionary with chapter and links
        """
        chapter_links = manga_page_html.select(self.conf['SERVER_CHAPTERS_TAG'])
        results = []
        for link in range(len(chapter_links)):
            results.append(dict(url=chapter_links[link].get("href"), chapter=chapter_links[link].get("title")))
        return results


    def get_chapter_page(self, chosen_chapter_url: str, single_page=True, page_number=1):
        """
        Returns the page with the images to be scraped by MangaWind.
        if single_page = False it uses the page_number variable to loop
        through the pages of the chapter that was chosen.
        """
        if single_page:
            image_tags = chosen_chapter_url.select(self.conf['SERVER_IMG_TAG'])
            images = []
            for image in image_tags:
                images.append(image.get('src'))
            return images
        else:
            pass
