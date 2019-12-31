import argparse
from manga_manipulation import MangaManipulation
import downloader

parser = argparse.ArgumentParser(
    prog='mangawind',
    description="MangaWind is a command-line utility for downloading and converting manga to pdf.",
    usage="""
        %(prog)s -s [manga]
        %(prog)s -s [manga] -c [manga index number] -n [number of chapters]""",
    epilog="""Use the -s flag for searching for manga and [-c][-n] flags to download them. If only one of them is provided it will
    either raise an error or not do anything."""
    )
parser.add_argument('-s', '--search',metavar='[manga]', type=str, help='Search for manga')
parser.add_argument('-c', '--choose', metavar='[manga index number]', type=int, help='Choose a manga')
parser.add_argument('-n', '--number-of-chapter', nargs='+', dest='chapters', metavar='[number of chapters]', type=str, help='Number of chapters to download')
parser.add_argument('--download-images', action='store_false', help='Download all the chapters as images')
args = parser.parse_args()

manga = MangaManipulation(args.search, args.choose)

def main():
    # Display the search result if -c is not used
    manga.run()
    # Take that input and download specified manga and chapters
    if args.chapters is not None:
        downloader.run(args.chapters, pdf_only=args.download_images)

if __name__ == "__main__":
        main()