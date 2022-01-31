import site_main
from helper import get_page_context
from leaky_cauldron.templator import render
from settings import TEMPLATE_DIR


class CategoriesPage:
    def __init__(self):
        self.page_name = 'categories.html'

    def __call__(self, request):
        # print(request)
        context = get_page_context(self.page_name)
        context['categories'] = site_main.training_site.categories
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body