import os.path

from jinja2 import Template, Environment, BaseLoader, FileSystemLoader

from settings import TEMPLATE_DIR, PROJECT_ROOT


def render(template_name, template_dir_path='', **kwargs):
    """
    Рендерит шаблон с параметрами
    :param template_dir_path: папка с шаблонами
    :param template_name: название шаблона
    :param kwargs: параметры для передачи в шаблон
    :return:
    """
    template_path = os.path.join(template_dir_path, template_name)
    with open(template_path, encoding='utf-8') as f:
        # template = Template(f.read())

        # запарился гуглить эту проблему
        template = Environment(loader=FileSystemLoader(f'{TEMPLATE_DIR}')).from_string(f.read())
        return template.render(**kwargs).encode('utf-8')


if __name__ == "__main__":
    output = render('index.html', TEMPLATE_DIR, context=[])
    print(output)
