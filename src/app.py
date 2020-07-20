from PyInquirer import prompt
from scrapers.searchmanga import list_of_search_results
from examples import custom_style_2

def manga_name():
    questions = [
        {
            'type': 'input',
            'name': 'manga_name',
            'message': 'Entre com o nome do manga',
        },
    ]
    return prompt(questions, style=custom_style_2)['manga_name']


def select_manga():
    questions = [
        {
            'type': 'list',
            'name': 'link_manga',
            'message': 'Seleciona o manga a ser baixado',
            'choices': list_of_search_results(str(manga_name())),
        },
    ]

    return prompt(questions, style=custom_style_2)['link_manga']

print(select_manga())
    