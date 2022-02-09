import pprint

from leaky_cauldron import NotFoundPage
from leaky_cauldron.helpers import parse_query_string, get_wsgi_input


class Application:
    routes = {}
    
    def __init__(self, fronts):
        self.fronts = fronts
    
    def __call__(self, environ, start_response):
        """
            :param environ: словарь данных от сервера
            :param start_response: функция для ответа серверу
            :return:
            """
        
        request = {}
        
        # pprint.pprint(environ)
        
        path = environ['PATH_INFO']
        if len(path) > 1 and path[-1] == '/':
            path = path[:-1]
        
        if path in self.routes:
            controller = self.routes[path]
        else:
            # тут смысл, чтобы можно было переопределить дефолтную 404 страницу
            controller = self.routes.get('not_found', NotFoundPage())
        
        wsgi_input = get_wsgi_input(environ)
        request_params = parse_query_string(environ['QUERY_STRING'])
        
        request['method'] = environ['REQUEST_METHOD']
        request['wsgi_input'] = wsgi_input
        request['request_params'] = request_params
        
        request.update({'user': 'blabla'})
        
        for front in self.fronts:
            front(request)
        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body]
    
    
#    def redirect(self, path, code=302, request=None, response=None):
#        if path in self.routes:
#            controller = self.routes[path]
#        else:
#            controller = self.routes.get('not_found', NotFoundPage())
#
#        code, body = controller(request)
#        return (code, [('Content-Type', 'text/html')])
#