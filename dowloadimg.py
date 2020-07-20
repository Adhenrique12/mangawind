from stringhelpers import * # String utility helpers
from settings import *      # Global constants
import shutil               # Do advanced file operations
import os                   # To operate with directories



# Download the image to the hard drive
def download_img(url, download_path, page):
    # Create the download path if it doesn't exist
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Assemble the page's image file path
    img_name = add_zeros(str(page)) + FILE_EXT
    img_path = download_path + img_name
    
    # Make a request but get binary data
    # Also, wait until it finishes downloading
    request  = send_request(url, True)
    
    # Create a binary file with an image extension
    # Get the decoded contents of the image stream
    # Copy them to the image path that we constructed
    with open(img_path, 'wb') as file_path:
        request.raw.decode_content = True
        shutil.copyfileobj(request.raw, file_path)
    
    print( DOWNLOADING_MESSAGE + str(page) )