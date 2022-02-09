from abc import ABC, abstractmethod
from enum import Enum
from typing import Union, List


class CourseType(Enum):
    WEBINAR = 'webinar'
    OFFLINE = 'offline'
    VIDEOS = 'videos'


class Course:
    """
    Обучающий курс
    """
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        self.teacher_name = kwargs.get('teacher_name')
        self.assign_students: List[Student] = []
    
    def __str__(self):
        return f'{self.__getattribute__("name")}'
    
    def add_student(self, student: 'Student'):
        self.assign_students.append(student)
    
    def remove_user(self, student: 'Student'):
        if student in self.assign_students:
            self.assign_students.remove(student)
    
    def update_course(self, **kwargs):
        self.__dict__.update(**kwargs)
        for student in self.assign_students:
            student.notify(self)


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
        return Course(**self.__course)


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
    
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.about = kwargs.get('about')
    
    def __repr__(self):
        return f'Teacher {self.name}'
    

class Student:
    def __init__(self, *args, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.about = kwargs.get('about')
    
    def __repr__(self):
        return f'{self.name}'
    
    def notify(self, course_: Course):
        print(f'Пользователю {self.name} пришло извещение!')
        print(f'Изменение курса {course_}')


class UserFactory:
    user_types = {
        'teacher': Teacher,
        'student': Student
    }
    
    @classmethod
    def create(cls, user_type: str, *args, **kwargs):
        if user_type not in cls.user_types:
            raise ValueError('Error! Wrong user type!')
        return cls.user_types[user_type](*args, **kwargs)


class TrainingSite:
    
    def __init__(self):
        self._students = []
        self._teachers = []
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
    
    def add_user(self, user: Union[Student, Teacher]):
        if isinstance(user, Student):
            self._students.append(user)
        else:
            self._teachers.append(user)
    
    def get_students(self, serial=False):
        if serial:
            return [student.__dict__ for student in self._students]
        else:
            return self._students
    
    @property
    def students(self):
        return self._students

if __name__ == '__main__':
    ts = TrainingSite()
    p = {
        'name': 'Python for beginners',
        'type': CourseType.WEBINAR.value,
        'teacher_name': 'Alex'
    }
    
    course = TrainingSite.create_course(p)
    print(course)
