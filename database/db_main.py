import sqlite3
from os.path import abspath, join, isdir
from pathlib import Path

from database.db_handler import DBHandler
from helper import students, teachers, courses
from models import CourseType

db_path = Path(__file__).parent.parent.absolute()
script_path = join(Path(__file__).parent.absolute(), 'create_db.sql')
conn = sqlite3.connect(join(db_path, 'db.sqlite'))

cursor = conn.cursor()

db_handler = DBHandler(conn)

with open(script_path) as f:
    cursor.executescript(f.read())


def populate_db():
    for student in students:
        db_handler.add_user(student['name'], student['email'], student['about'], 'student')
    for teacher in teachers:
        db_handler.add_user(teacher['name'], teacher['email'], teacher['about'], 'teacher')
    
    for course in courses:
        db_handler.add_course(course['name'], course['type'], course['teacher_name'])

# populate_db()
