import sqlite3
from os.path import abspath, join, isdir
from pathlib import Path

# from database.db_concrete_mappers import SQLiteStudentMapper, SQLiteCourseMapper, SQLiteTeacherMapper
from database.unit_of_work import UnitOfWork
from helper import students, teachers, courses
from models import Student, Teacher, Course

db_path = Path(__file__).parent.parent.absolute()
script_path = join(Path(__file__).parent.absolute(), 'create_db.sql')
conn = sqlite3.connect(join(db_path, 'db.sqlite'))

cursor = conn.cursor()

# student_mapper = SQLiteStudentMapper(conn)
# teacher_mapper = SQLiteTeacherMapper(conn)
# course_mapper = SQLiteCourseMapper(conn)

with open(script_path) as f:
    cursor.executescript(f.read())


def populate_db():
    for student in students:
        student = Student(name=student['name'], email=student['email'], about=student['about'])
        student.mark_new()
    for teacher in teachers:
        teacher = Teacher(name=teacher['name'], email=teacher['email'], about=teacher['about'])
        teacher.mark_new()
    for course in courses:
        course = Course(name=course['name'], type=course['type'], teacher_name=course['teacher_name'])
        course.mark_new()
    
    UnitOfWork.get_current().commit()


populate_db()
