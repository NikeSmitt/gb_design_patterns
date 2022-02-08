import site_main
from leaky_cauldron.helpers import fix_url_str
from leaky_cauldron.routes import app
from leaky_cauldron.templator import render
from models import Course
from settings import TEMPLATE_DIR
from site_main import training_site


@app('/editcourse')
class EditCourse:
    
    def __init__(self):
        self.page_name = 'editcourse.html'
    
    def __call__(self, request):
        if request['method'] == 'POST':
            data = request.get('wsgi_input')
            if data:
                old_course_name = fix_url_str(data.pop('original_course_name', None))
                if old_course_name is None:
                    raise KeyError("Something wrong with original_course_name!!!!")
                course_to_edit: Course = list(filter(lambda course: course.name == old_course_name, training_site.courses))[0]
                course_to_edit.update_course(**data)
                
            body = render('redirect.html', TEMPLATE_DIR)
            return '302 OK', body
                
        course_name = request['request_params'].get('course')
        course_name = fix_url_str(course_name)
        context = None
        if course_name:
            course_to_edit = list(filter(lambda course: course.name == course_name, training_site.courses))[0]
            context = {'course': course_to_edit.__dict__}
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body
