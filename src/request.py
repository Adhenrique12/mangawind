import settings        # Global constants
import requests        # Library to make HTTP requests

# Send a request via HTTP
def send_request(url, binary = False):
    try: # Brace for possible connection exceptions
        request = requests.get(url, stream = binary) # HTTP request to 
    except: # What to do if somethig happens
        print("Error ...") # Print a message before exiting
        exit() # Exit the program on a connection failure
    print(request)
    return request # If successful, return the request



