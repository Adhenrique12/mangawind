from PyInquirer import prompt, Separator
from searchmanga import list_of_search_results
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
    questions = [
        {
                'type': 'checkbox',
                'qmark': 'Ⓜ📃',
                'message': 'Select toppings',
                'name': 'toppings',
                'choices': [ 
                            Separator('= Capitulos ='),
                                    {
                                        'name': 'Ham'
                                    },
                                    {
                                        'name': 'Ground Meat'
                                    },
                                    {
                                        'name': 'Bacon'
                                    },
            
                            ],
                'validate': lambda answer: 'You must choose at least one topping.' \
                if len(answer) == 0 else True
        }
    ]

    answers = prompt(questions, style=custom_style_2)
   
print(select_manga())

#lista_dicionario = []
#manga_link = {'manga': 'naruto'}
#manga_link = {'manga': 'naruto1'}
#manga_link = {'manga': 'naruto2'}
#lista_dicionario.append(manga_link)
#print(lista_dicionario[0])
    