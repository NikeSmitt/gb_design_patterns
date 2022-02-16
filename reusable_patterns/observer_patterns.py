from abc import ABC, abstractmethod


class Observer(ABC):
    
    @abstractmethod
    def notify(self, subject):
        pass


class Observable(ABC):
    
    @abstractmethod
    def subscribe(self, observer):
        pass
    
    @abstractmethod
    def remove_subscriber(self, observer):
        pass
    
    @abstractmethod
    def notify_observers(self):
        pass
