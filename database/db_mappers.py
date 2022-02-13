import sqlite3
from abc import ABC, abstractmethod


class BaseMapper(ABC):
    @abstractmethod
    def execute(self, sql: str,
                params: tuple = (),
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False
                ):
        pass


class SQLiteBaseMapper(BaseMapper):
    
    def __init__(self, connection):
        self.conn = connection
        self.cursor = self.conn.cursor()
    
    def execute(self, sql: str,
                params: tuple = (),
                fetchone: bool = False,
                fetchall: bool = False,
                commit: bool = False
                ):
        data = None
        try:
            self.cursor.execute(sql, params)
            if commit:
                self.conn.commit()
            elif fetchone:
                data = self.cursor.fetchone()
            elif fetchall:
                data = self.cursor.fetchall()
        except sqlite3.Error as e:
            print(e)
        return data


class UserMapper(ABC):
    @abstractmethod
    def add(self, student):
        pass
    
    @abstractmethod
    def get_by_name(self, name):
        pass
    
    @abstractmethod
    def get_all(self):
        pass


class CourseMapper(ABC):
    
    @abstractmethod
    def add(self, course):
        pass
    
    @abstractmethod
    def get_course(self, by_type: str = None, by_teacher_name: str = None):
        pass