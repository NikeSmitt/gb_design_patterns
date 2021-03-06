from helper import get_page_context, get_covid_info
from leaky_cauldron.helpers import debug
from leaky_cauldron.routes import app
from settings import TEMPLATE_DIR
from leaky_cauldron.templator import render


@app('/')
# @debug
class IndexPage:
    def __init__(self):
        self.page_name = 'index.html'
    
    def __call__(self, request):
        context = get_page_context(self.page_name)
        if request.get('covid'):
            context['covid'] = get_covid_info()
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body
