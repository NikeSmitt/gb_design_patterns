from leaky_cauldron import Application
import collections

from controllers.fronts import secret_front, other_front


application = Application([secret_front, other_front])
# print(f'{application.routes=}')