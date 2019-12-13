import click
from manga_manipulation import MangaManipulation
import downloader

@click.group()
def main():
    pass

@main.command()
@click.argument('search')
def search(search):
    manga = MangaManipulation()
    manga.manga = search
    return manga.search_result(manga.manga)

if __name__ == '__main__':
    main()