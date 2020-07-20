# The manga provider to download the pages from
PROVIDER = "https://mangakakalot.com/"

# The manga search engine
SEARCH = "https://manganelo.com/search/story/" # + seriesName

# The folder where the episode is going to be saved
MANGA_PATH = "/home/adelio/Pictures/" # + seriesName/epNumber/

# Determines from which page number to start looping
INITIAL_PAGE = 1

# Message displayed at the end of the dowload loop
SUCCESS_MESSAGE = "The episode has been successfully downloaded!"

# Message to be displayed while downloading a page
DOWLOADING_MESSAGE = "Currently downloading page #" # + pageNumber

# Message to be displayed when the episode isn't released yet
NOT_RELEASED_MESSAGE = "This episode hasn't been released yet... sorry, mate."

# Message to be displayed for HTTP request errors
DOESNT_EXIST = "This series doesn't exist in the database!"

# Maximum amount of digits expected as the page number
ESTIMATED_MAX_DIGITS = 3

# The extension of the image file in the URL
FILE_EXT = ".jpg"