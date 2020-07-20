from bs4 import BeautifulSoup as bs # The source code parser
from settings import *              # Global constants
from request import *               # Requesting and downloading
from stringhandler import *         # String utility helpers
import sys                          # To grab the arguments
import searchmanga                  # To grab the link of the manga

def download_manga_episode(seriesName, episodeNum):
    current_page  = INITIAL_PAGE
    download_path = get_download_path(seriesName, episodeNum)

    # Exit the function if the episode hasn't been released yet
    if not_released_yet(seriesName, episodeNum):
        print(NOT_RELEASED_MESSAGE)
        return None

    while True: # Loop through the pages until the last one
        manga_url = ge_manga_url(seriesName, episodeNum, current_page)
        page_url  = get_page_url(seriesName, episodeNum, current_page)
        request   = send_request(page_url)
        raw_html  = request.text
        
        # If the page or manga doesn't exist...
        if request.status_code != 200 or not len(raw_html):
            print(DOESNT_EXIST if not len(raw_html) else SUCCESS_MESSAGE)
            break # Exit the loop and end the script
                
        # Scrap the html to find the page's image link
        parsed_html = bs(raw_html, "html.parser")
        img_url     = parsed_html.find("img", {"id": "img"}).get("src")
        
        # Save the page's image in the download path
        download_img(img_url, download_path, current_page)
        
        # Change the current page to the next one
        current_page = current_page + 1

# Run the main function in the console
download_manga_episode(sys.argv[1], sys.argv[2])