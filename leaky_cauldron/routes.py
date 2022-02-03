from leaky_cauldron import Application


def app(url):
    def decorator(obj):
        Application.routes[url] = obj()
        
        def wrapper(request):
            return obj(request)
        
        return wrapper
    
    return decorator
