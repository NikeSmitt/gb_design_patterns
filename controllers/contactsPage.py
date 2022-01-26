from helper import get_page_context
from leaky_cauldron.helpers import fix_url_str
from settings import TEMPLATE_DIR
from leaky_cauldron.templator import render
from urllib.parse import unquote


class ContactsPage:
    def __init__(self):
        self.page_name = 'contacts.html'

    def __call__(self, request):
        # print(request)
        if request['method'] == 'POST':
            data = request.get('wsgi_input')
            if data:
                topic = fix_url_str(data['topic'])
                email = fix_url_str(data['email'])
                message = fix_url_str(data['message'])

                print(f'User has sent:\n'
                      f'topic - {topic}\n'
                      f'email - {email}\n'
                      f'message: {message}')

        context = get_page_context(self.page_name)
        body = render(self.page_name, TEMPLATE_DIR, context=context)
        return '200 OK', body
