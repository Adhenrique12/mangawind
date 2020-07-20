from stringhanders import * # String utility helpers
from settings import *      # Global constants
import requests             # Library to make HTTP requests

# Send a request via HTTP
def send_request(url, binary = False):
    try: # Brace for possible connection exceptions
        request = requests.get(url, stream = binary) # HTTP request to 
    except: # What to do if somethig happens
        print("Error ...") # Print a message before exiting
        exit() # Exit the program on a connection failure
    print(request)
    return request # If successful, return the request

# Check to see if the episode was or not released
def not_released_yet(seriesName, episodeNum):
    manga_url = get_page_url(seriesName, episodeNum)
    html      = send_request(manga_url).text
    
    return NOT_RELEASED_TEXT in html

