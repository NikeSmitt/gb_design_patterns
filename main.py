from pprint import pprint

from controllers.fronts import secret_front, other_front
from controllers.notFoundPage import NotFoundPage
from urls import routes


class Application:
    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        """
            :param environ: словарь данных от сервера
            :param start_response: функция для ответа серверу
            :return:
            """
        path = environ['PATH_INFO']
        if len(path) > 1 and path[-1] == '/':
            path = path[:-1]
        if path in self.routes:
            controller = self.routes[path]
        else:
            controller = NotFoundPage()

        request = {'user': 'blabla'}
        for front in self.fronts:
            front(request)
        code, body = controller(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body]


application = Application(routes, [secret_front, other_front])
