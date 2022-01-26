from helper import get_page_context
from settings import TEMPLATE_DIR
from leaky_cauldron.templator import render


class AboutPage:
    def __init__(self):
        self.page_name = 'about.html'

    def __call__(self, request):
        print(request)
        context = get_page_context(self.page_name)
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body
