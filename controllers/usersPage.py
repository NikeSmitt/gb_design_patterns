from database.db_main import student_mapper
from helper import get_page_context
from leaky_cauldron.helpers import fix_url_str
from leaky_cauldron.routes import app
from leaky_cauldron.templator import render
from models import UserFactory
from settings import TEMPLATE_DIR
from site_main import training_site


@app('/users')
class UsersPage:
    
    def __init__(self):
        self.page_name = 'users.html'
    
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request.get('wsgi_input')
            if data:
                user_type = data['userType'] if 'userType' in data else 'student'
                normalize_data = {k: fix_url_str(v) for k, v in data.items()}
                user = UserFactory.create(user_type, **normalize_data)
                student_mapper.add_user(normalize_data['name'], normalize_data['email'], normalize_data['about'])
                training_site.add_user(user)
        context = get_page_context(self.page_name)
        saved_students = training_site.get_students(serial=True)
        context['users']['students'].extend(saved_students)
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body
