# просто эмуляция crud чтобы
import random


def get_page_context(page_name=''):
    context = {}
    if page_name == 'index.html':
        context = {
            'navigation': [{'title': 'Home', 'href': '/', 'is_active': 'true'},
                           {'title': 'About', 'href': '/about', 'is_active': 'false'},
                           {'title': 'News', 'href': '/news', 'is_active': 'false'}],
            'info': 'This is my first home-task',

        }

    elif page_name == 'about.html':
        context = {
            'navigation': [{'title': 'Home', 'href': '/', 'is_active': 'false'},
                           {'title': 'About', 'href': '/about', 'is_active': 'true'},
                           {'title': 'News', 'href': '/news', 'is_active': 'false'}],
            'info': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                    'the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                    'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                    'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                    'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                    'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                    'Lorem Ipsum. '
        }

    return context


def is_user_covid_free():
    # просто чтобы... ну там...
    return random.choice([True, False])


def get_covid_info():
    return f'У тебя COVID! Оставайся дома и береги себя!'
