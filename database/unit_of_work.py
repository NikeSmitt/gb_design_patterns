import threading
from abc import ABC

from database.mapper_registry import MapperRegistry


class UnitOfWork:
    current = threading.local()
    
    def __init__(self):
        self.new_objects = []
        self.dirty_objects = []
        self.removed_objects = []
    
    def add_new(self, obj):
        self.new_objects.append(obj)
    
    def add_dirty(self, obj):
        self.dirty_objects.append(obj)
    
    def add_removed(self, obj):
        self.removed_objects.append(obj)
    
    def commit(self):
        self.insert_new()
        self.update_dirty()
        self.delete_removed()
    
    def insert_new(self):
        for obj in self.new_objects:
            MapperRegistry.get_mapper(obj).add(obj)
    
    def update_dirty(self):
        pass
    
    def delete_removed(self):
        pass
    
    @classmethod
    def set_current(cls, unit_of_work):
        cls.current.unit_of_work = unit_of_work
    
    @classmethod
    def new_current(cls):
        cls.set_current(UnitOfWork())
    
    @classmethod
    def get_current(cls) -> 'UnitOfWork':
        return cls.current.unit_of_work


class DomainObject(ABC):
    def mark_new(self):
        UnitOfWork.get_current().add_new(self)
    
    def mark_dirty(self):
        UnitOfWork.get_current().add_dirty(self)
    
    def mark_removed(self):
        UnitOfWork.get_current().add_removed(self)