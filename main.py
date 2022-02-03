from leaky_cauldron import Application

from controllers.fronts import secret_front, other_front


application = Application([secret_front, other_front])
