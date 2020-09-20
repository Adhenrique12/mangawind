import cloudscraper # type: ignore

# Initialize scraper with firefox user_agent
scraper = cloudscraper.create_scraper('firefox')
# Send a request via HTTP
def send_request(url, binary=False):
    '''
    Checks if the page exists and if it does it proceeds with a GET request
    '''
    try:
        request = scraper.get(url, stream = binary)
    except:
        print(f"Could not connect with: {url}")
        exit()
    return request
