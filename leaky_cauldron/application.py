from pprint import pprint
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
        
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # подскажите как сделать по-другому
        import controllers
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        request = {}

        path = environ['PATH_INFO']
        if len(path) > 1 and path[-1] == '/':
            path = path[:-1]
        
        if path in self.routes:
            controller = self.routes[path]
        else:
            # тут смысл, чтобы можно было переопределить дефолтную 404 страницу
            controller = self.routes.get('not_found', NotFoundPage())

        # pprint(environ)

        wsgi_input = get_wsgi_input(environ)
        request_params = parse_query_string(environ['QUERY_STRING'])

        request['method'] = environ['REQUEST_METHOD']
        request['wsgi_input'] = wsgi_input
        request['request_params'] = request_params

        request.update({'user': 'blabla'})

        # print(request)

        for front in self.fronts:
            front(request)
        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body]
