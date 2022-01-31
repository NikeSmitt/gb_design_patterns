from abc import ABC, abstractmethod
from enum import Enum


class CourseType(Enum):
    WEBINAR = 'webinar'
    OFFLINE = 'offline'
    VIDEOS = 'videos'


class Course:
    """
    Обучающий курс
    """
    
    def __init__(self, params):
        self.params = params
    
    def __str__(self):
        return f'{self.params}'


class CourseCategory:
    """Категория обучающего курса"""
    
    def __init__(self, name):
        self.name = name
        self.courses = []
    
    def add_course(self, course: Course):
        self.courses.append(course)
    
    def __str__(self):
        return f'{self.name}'

class AbsBuilder(ABC):
    
    @abstractmethod
    def reset(self):
        pass
    
    @abstractmethod
    def build(self):
        pass


class CourseBuilder(AbsBuilder):
    def reset(self):
        pass
    
    def __init__(self):
        self.__course = {
            'name': None,
            'type': None,
            'teacher_name': None
        }
    
    def set_name(self, name: str):
        self.__course['name'] = name
        return self
    
    def set_course_type(self, course_type: CourseType):
        self.__course['type'] = course_type
        return self
    
    def set_teacher(self, teacher_name: str):
        self.__course['teacher_name'] = teacher_name
        return self
    
    def build(self):
        return Course(self.__course)


class CategoryBuilder(AbsBuilder):
    def build(self):
        return CourseCategory(self.__category['name'])
    
    def reset(self):
        pass
    
    def __init__(self):
        self.__category = {}
    
    def set_name(self, name: str):
        self.__category['name'] = name
        return self


class Teacher:
    pass


class Student:
    pass


class UserFactory:
    user_types = {
        'teacher': Teacher,
        'student': Student
    }
    
    @classmethod
    def create(cls, user_type: str):
        if user_type not in cls.user_types:
            raise ValueError('Error! Wrong user type!')
        return cls.user_types[user_type]()


class TrainingSite:
    
    def __init__(self):
        self.students = []
        self.teachers = []
        self.courses = []
        self.categories = []
    
    @staticmethod
    def create_user(type_):
        return UserFactory.create(type_)
    
    @staticmethod
    def create_course(params: dict):
        course_builder = CourseBuilder()
        return course_builder \
            .set_name(params['name']) \
            .set_course_type(params['type']) \
            .set_teacher(params['teacher_name']) \
            .build()
    
    @staticmethod
    def create_course_category(params: dict):
        category_builder = CategoryBuilder()
        return category_builder.set_name(params['name']).build()


if __name__ == '__main__':
    ts = TrainingSite()
    p = {
        'name': 'Python for beginners',
        'type': CourseType.WEBINAR,
        'teacher_name': 'Alex'
    }
    
    course = TrainingSite.create_course(p)
    print(course)
