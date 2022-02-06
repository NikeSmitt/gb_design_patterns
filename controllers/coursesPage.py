import site_main
from helper import get_page_context
from main import application
from leaky_cauldron.templator import render
from settings import TEMPLATE_DIR


@application.route('/courses')
class CoursesPage:
    def __init__(self):
        self.page_name = 'courses.html'

    def __call__(self, request):
        # print(request)
        context = get_page_context(self.page_name)
        courses = site_main.training_site.courses
        context['courses'] = [course for course in site_main.training_site.courses]
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body