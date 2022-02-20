from datetime import datetime

from reusable_patterns.observer_patterns import Observer, Observable
from reusable_patterns.singleton import SingletonLoggerMeta

CRITICAL = 'CRITICAL'
ERROR = 'ERROR'
WARNING = 'WARNING'
DEBUG = 'DEBUG'
INFO = 'INFO'


class LoggerHandler:
    _levels = [DEBUG, INFO, WARNING, ERROR, CRITICAL]
    
    def __init__(self):
        self.__log_level_idx = 0
        self.__format = '%(name)s - %(level_name)s - %(message)s'
    
    def set_level(self, level):
        try:
            idx = self._levels.index(level)
        except ValueError as e:
            print(e)
        else:
            self.__log_level_idx = idx
    
    def set_formatter(self, format_: str):
        self.__format = format_
    
    def _is_level_approved(self, call_level):
        idx_call = self._levels.index(call_level)
        return idx_call >= self.__log_level_idx
    
    def _formatting(self, name, level_name, message):
        return self.__format % {'time': datetime.now(),
                                'name': name,
                                'level_name': level_name,
                                'message': message}


class StreamHandler(LoggerHandler, Observer):
    
    def notify(self, subject):
        if self._is_level_approved(subject.current_level):
            print(self._formatting(subject.name, subject.current_level, subject.current_message))


class FileHandler(LoggerHandler, Observer):
    
    def __init__(self, file_name: str):
        super().__init__()
        self.file_name = file_name
    
    def notify(self, subject):
        if self._is_level_approved(subject.current_level):
            message = self._formatting(subject.name, subject.current_level, subject.current_message)
            self.__write(message)
    
    def __write(self, message):
        with open(self.file_name, 'a', encoding='utf-8') as f:
            f.write(f'{message}\n')


class Logger(Observable):
    __metaclass__ = SingletonLoggerMeta
    
    def __init__(self, name='default'):
        self.name = name
        self.__handlers = set()
        self.current_level = None
        self.current_message = None
    
    def remove_subscriber(self, observer):
        pass
    
    def notify_observers(self):
        for handler in self.__handlers:
            handler.notify(self)
    
    def subscribe(self, observer):
        self.__handlers.add(observer)
    
    def error(self, message):
        self.current_level = ERROR
        self.current_message = message
        self.notify_observers()
    
    def critical(self, message):
        self.current_level = CRITICAL
        self.current_message = message
        self.notify_observers()
    
    def warning(self, message):
        self.current_level = WARNING
        self.current_message = message
        self.notify_observers()
    
    def debug(self, message):
        self.current_level = DEBUG
        self.current_message = message
        self.notify_observers()
    
    def info(self, message):
        self.current_level = INFO
        self.current_message = message
        self.notify_observers()


if __name__ == '__main__':
    logger_1 = Logger()
    logger_2 = Logger('main')
    
    stream_handler = StreamHandler()
    stream_handler.set_level(INFO)
    stream_handler.set_formatter('%(time)s - %(name)s - %(level_name)s - %(message)s')
    
    file_handler = FileHandler('temp.log')
    file_handler.set_level(WARNING)
    file_handler.set_formatter('%(level_name)s ::: %(message)s')
    
    logger_1.subscribe(file_handler)
    logger_2.subscribe(stream_handler)
    
    # print(logger_1 is logger_2)
    # print(logger_2 is Logger('main'))
    
    logger_2.error('Now you can log what you want')
    logger_1.error('Error here')
    
    logger_2.info('Now you can log what you want')
