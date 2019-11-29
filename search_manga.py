from bs4 import BeautifulSoup
import requests as r

website = "https://mangakakalot.com/"

def chosen_manga():
    def search_result() -> str:
        manga = input("What manga do you want to search for? ")
        manga = manga.replace(' ', '_')
        search = r.post(website + 'search/' + manga)
        # Return the search result as html
        return search.text

    def manga_choice() -> list:
        print('These are the results: \n')
        choices = []
        counter = 0
        for link in soup.find_all('h3', class_='story_name'):
            counter += 1
            choices.append(link.a['href'])
            # Print a numbered list of the search result
            print(counter, link.a.text)
        # Return the list of links from the search result
        return choices

    def choose_manga(manga_links):
        choices = manga_links
        choice = int(input("Type the number of the manga of your choice "))
        print(choices)
        return choices[choice - 1]

    soup = BeautifulSoup(search_result(), 'lxml')
    return choose_manga(manga_choice())