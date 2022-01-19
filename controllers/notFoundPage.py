class NotFoundPage:
    def __call__(self, *args, **kwargs):
        return '404 Not Found', b'404 page not found'
