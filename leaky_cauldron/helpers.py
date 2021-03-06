import functools
import time
from urllib.parse import unquote


def parse_query_string(s: str) -> dict:
    output = {}
    if s:
        key_values = s.split('&')
        
        for pair in key_values:
            k, v = pair.split('=')
            output[k] = v
    
    return output


def get_wsgi_input(env) -> dict:
    output = {}
    if env['REQUEST_METHOD'] == 'POST':
        content_length = int(env.get('CONTENT_LENGTH', 0))
        data = env['wsgi.input'].read(content_length).decode(encoding='utf-8')
        output = parse_query_string(data)
    return output


def fix_url_str(s: str) -> str:
    output = s.replace('+', '%20')
    return unquote(output)


def debug(obj):
    @functools.wraps(obj)
    def wrapped_debug(*args, **kwargs):
        print(f'Calling {obj.__name__!r}')
        start = time.perf_counter()
        values = obj(*args, **kwargs)
        print(f'Время выполнения: {time.perf_counter() - start}')
        return values
    
    return wrapped_debug
