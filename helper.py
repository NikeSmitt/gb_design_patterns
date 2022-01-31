# просто эмуляция crud чтобы
import random

from models import CourseType


def get_page_context(page_name=''):
    context = {}
    navigation = [{'title': 'Home', 'href': '/', 'is_active': 'true'},
                  {'title': 'About', 'href': '/about', 'is_active': 'false'},
                  {'title': 'Contacts', 'href': '/contacts', 'is_active': 'false'},
                  {'title': 'Categories', 'href': '/categories', 'is_active': 'false'},
                  {'title': 'Courses', 'href': '/courses', 'is_active': 'false'}, ]
    if page_name == 'index.html':
        context = {
            
            'info': 'This is my first home-task',
            
        }
    
    elif page_name == 'about.html':
        context = {
            'info': 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been '
                    'the industry s standard dummy text ever since the 1500s, when an unknown printer took a galley '
                    'of type and scrambled it to make a type specimen book. It has survived not only five centuries, '
                    'but also the leap into electronic typesetting, remaining essentially unchanged. It was '
                    'popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, '
                    'and more recently with desktop publishing software like Aldus PageMaker including versions of '
                    'Lorem Ipsum. '
        }
    
    context['navigation'] = navigation
    return context


def is_user_covid_free():
    # просто чтобы... ну там...
    return random.choice([True, False])


def get_covid_info():
    return f'У тебя COVID! Оставайся дома и береги себя!'


courses = [
    {'name': 'Python Faculty', 'type': CourseType.WEBINAR, 'teacher_name': 'Vernon'},
    {'name': 'Java Faculty', 'type': CourseType.WEBINAR, 'teacher_name': 'Harry'},
    {'name': 'Kotlin Faculty', 'type': CourseType.WEBINAR, 'teacher_name': 'Elly'},
    {'name': 'iOS developer course', 'type': CourseType.WEBINAR, 'teacher_name': 'Ron'}
]

categories = [
    {'name': 'Python'},
    {'name': 'Java'},
    {'name': 'Go'},
    {'name': 'JavaScript'},
    {'name': 'Swift'},
    {'name': 'Kotlin'},
]
