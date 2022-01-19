from model import is_user_covid_free


def secret_front(request):
    if is_user_covid_free():
        request['covid'] = True


def other_front(request):
    request['key'] = 'value'

