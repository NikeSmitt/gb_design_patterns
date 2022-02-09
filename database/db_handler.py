import sqlite3

from models import CourseType


class DBHandler:
    
    def __init__(self, connection: sqlite3.Connection):
        self.conn = connection
        self.cursor = connection.cursor()
    
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
    
    def get_all_students(self):
        sql = "SELECT name, email, about FROM students;"
        return self.execute(sql, fetchall=True)
    
    def add_user(self, name: str, email: str, about: str, user_type: str):
        user_type = f'{user_type}s'
        sql = f"INSERT INTO {user_type} (id, name, email, about) VALUES (?, ?, ?, ?)"
        params = (None, name, email, about)
        self.execute(sql, params, commit=True)
    
    def get_teacher(self, name: str = None, id_: int = None):
        if name is not None:
            sql = "SELECT * FROM teachers WHERE name=?"
            params = (name,)
            return self.execute(sql, params, fetchone=True)
        if id_ is not None:
            sql = "SELECT * FROM teachers WHERE id=?"
            return self.execute(sql, (id_,), fetchone=True)
    
    def add_course(self, name: str, type_: str, teacher_name: str):
        teacher_id = self.get_teacher(name=teacher_name)[0]
        sql = "INSERT INTO courses (id, name, type, teacherId) VALUES (?,?,?,?)"
        params = (None, name, type_, teacher_id)
        self.execute(sql, params, commit=True)
        
    def get_course(self, by_type: str = None, by_teacher_name: str = None):
        sql = "SELECT courses.name, courses.type, teachers.name " \
              "FROM courses JOIN teachers ON courses.teacherId = teachers.id;"
        params = ()
        if by_type is not None:
            sql = f'{sql} WHERE courses.type=?'
            params = by_type,
        elif by_teacher_name is not None:
            sql = f'{sql} WHERE courses.teacherId=?'
            teacher_id = self.get_teacher(name=by_teacher_name)[0]
            params = teacher_id,
        return self.execute(sql, params, fetchall=True)
        
        
