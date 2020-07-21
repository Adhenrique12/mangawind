import settings        # Global constants
import requests        # Library to make HTTP requests

# Send a request via HTTP
def send_request(url, binary = False):
    try: 
        request = requests.get(url, stream = binary)  
    except: 
        print("Error ...") 
        exit() 
    
    return request 



