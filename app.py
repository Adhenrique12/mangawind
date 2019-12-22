import argparse
from manga_manipulation import MangaManipulation
import downloader

parser = argparse.ArgumentParser(
    description="A command-line utility for downloading manga"
)
parser.add_argument('-s', '--search', type=str, help='Search for manga')
parser.add_argument('-c', '--choose', type=int, help='Choose a manga')
parser.add_argument('-n', '--number-of-chapter', dest='chapters', type=str, help='Number of chapters to download')
args = parser.parse_args()

manga = MangaManipulation(args.search, args.choose)

def main():
    # Display the search result if -c is not used
    manga.run()
    # Take that input and download specified manga and chapters
    if args.chapters is not None:
        downloader.run(args.chapters)

if __name__ == "__main__":
    main()