class SingletonMeta(type):
    
    # __instance = {}
    
    def __init__(cls, name, base, attrs, **kwargs):
        super().__init__(name, base, attrs)
        cls.__instance = {}
    
    def __call__(cls, *args, **kwargs):
        name = None
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']
        
        if name and name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]
