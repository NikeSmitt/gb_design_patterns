# просто эмуляция crud чтобы
import random

from models import CourseType


def get_page_context(page_name=''):
    context = {}
    navigation = [{'title': 'Home', 'href': '/', 'is_active': 'true'},
                  {'title': 'About', 'href': '/about', 'is_active': 'false'},
                  {'title': 'Contacts', 'href': '/contacts', 'is_active': 'false'},
                  {'title': 'Categories', 'href': '/categories', 'is_active': 'false'},
                  {'title': 'Courses', 'href': '/courses', 'is_active': 'false'},
                  {'title': 'Users', 'href': '/users', 'is_active': 'false'},
                  ]
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
    elif page_name == 'users.html':
        context = {
            'users': {
                'teachers': [],
                'students': [],
            }
        }
    
    context['navigation'] = navigation
    return context


def is_user_covid_free():
    # просто чтобы... ну там...
    return random.choice([True, False])


def get_covid_info():
    return f'У тебя COVID! Оставайся дома и береги себя!'


courses = [
    {'name': 'Python Faculty', 'type': CourseType.WEBINAR.value, 'teacher_name': 'Albus Dumbledore'},
    {'name': 'Java Faculty', 'type': CourseType.WEBINAR.value, 'teacher_name': 'Severus Snape'},
    {'name': 'Kotlin Faculty', 'type': CourseType.WEBINAR.value, 'teacher_name': 'Albus Dumbledore'},
    {'name': 'iOS developer course', 'type': CourseType.WEBINAR.value, 'teacher_name': 'Minerva McGonagall'}
]

categories = [
    {'name': 'Python'},
    {'name': 'Java'},
    {'name': 'Go'},
    {'name': 'JavaScript'},
    {'name': 'Swift'},
    {'name': 'Kotlin'},
]

students = [
    {'name': 'Ronald Weasley',
     'email': 'redhead@hogwarts.wis',
     'about': 'English pure-blood wizard, the sixth and youngest son of Arthur and Molly Weasley'},
    {'name': 'Neville Longbottom',
     'email': 'neville@hogwarts.wis',
     'about': ' British pure-blood wizard, the only child and son of Frank and Alice Longbottom'},
    {'name': 'Draco Malfoy',
     'email': 'draco@hogwarts.wis',
     'about': "Slytherin student in Harry's year. Quidditch Seeker, prefect, and member "
                                           "of the Inquisitorial Squad."},
]

teachers = [
    {'name': 'Minerva McGonagall',
     'email': 'minerva@hogwarts.wis',
     'about': 'Hogwarts Transfiguration professor, Head of Gryffindor House, Deputy Headmistress of Hogwarts, '
              'and member of the Order of the Phoenix'},
    {'name': 'Albus Dumbledore',
     'email': 'theheadmaster@hogwarts.wis',
     'about': "Transfiguration professor in Tom Riddle's time, and Hogwarts headmaster in Harry Potter's time. "
              "Founder of the Order of the Phoenix."},
    {'name': 'Severus Snape',
     'email': 'severus@hogwarts.wis',
     'about': "Potions and later Defence Against the Dark Arts professor at Hogwarts. Head of Slytherin House"},
]