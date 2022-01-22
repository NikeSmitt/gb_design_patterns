from leaky_cauldron import Application

from controllers.fronts import secret_front, other_front
from urls import routes


application = Application(routes, [secret_front, other_front])
