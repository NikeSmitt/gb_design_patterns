class SingletonLoggerMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        name = None
        if args:
            name = args[0]
        elif 'name' in kwargs:
            name = kwargs['name']
        if name not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[name] = instance
        return cls._instances[name]