from PyInquirer import prompt, Separator
from searchmanga import list_of_search_results, list_of_all_chapters
from examples import custom_style_2

def manga_name():
    questions = [
        {
            'type': 'input',
            'name': 'manga_name',
            'message': 'Entre com o nome do manga',
        },
    ]
    manga = prompt(questions, style=custom_style_2)['manga_name']
    
    return "_".join( manga.split(" ") ).lower()


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

def select_chapters_to_download():
    
    lista_chapters = list_of_all_chapters(select_manga())
    lista_final = [Separator('= List of Chapters =')]

    for x in lista_chapters:
        dicionario = dict(name=x)
        lista_final.append(dicionario)
    
    
    questions = [
        {
                'type': 'checkbox',
                'qmark': 'Ⓜ  📃',
                'message': 'Select toppings',
                'name': 'toppings',
                'choices': lista_final,
                'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]
    
    return prompt(questions, style=custom_style_2)
   
print(select_chapters_to_download())


    