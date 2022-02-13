from database.db_mappers import SQLiteBaseMapper, UserMapper, CourseMapper
from models import Student, Teacher, Course


class SQLiteStudentMapper(SQLiteBaseMapper, UserMapper):
    
    def __init__(self, connection):
        super().__init__(connection)
    
    def add(self, student: Student):
        sql = f"INSERT INTO students (id, name, email, about) VALUES (?, ?, ?, ?)"
        params = (None, student.name, student.email, student.about)
        self.execute(sql, params, commit=True)
    
    def get_by_name(self, name):
        sql = "SELECT * FROM students WHERE name=?"
        params = (name,)
        student_data = self.execute(sql, params, fetchone=True)
        if student_data is not None:
            id_, name_, email_, about_ = student_data
            return Student(id=id_, name=name_, email=email_, about=about_)
    
    def get_all(self):
        sql = "SELECT name, email, about FROM students "
        params = ()
        students_data = self.execute(sql, params, fetchall=True)
        output = []
        for name_, email_, about_ in students_data:
            output.append(Student(name=name_, email=email_, about=about_))
        return output


class SQLiteTeacherMapper(SQLiteBaseMapper, UserMapper):
    
    def __init__(self, connection):
        super().__init__(connection)
    
    def add(self, teacher: Teacher):
        sql = f"INSERT INTO teachers (id, name, email, about) VALUES (?, ?, ?, ?)"
        params = (None, teacher.name, teacher.email, teacher.about)
        self.execute(sql, params, commit=True)
    
    def get_all(self):
        sql = "SELECT id, name, email, about FROM teachers"
        params = ()
        teachers_data = self.execute(sql, params, fetchall=True)
        output = []
        for id_, name_, email_, about_ in teachers_data:
            output.append(Teacher(id=id_, name=name_, email=email_, about=about_))
        
        return output
    
    def get_by_name(self, name: str):
        sql = "SELECT * FROM teachers WHERE name=?"
        params = (name,)
        teacher_data = self.execute(sql, params, fetchone=True)
        if teacher_data is not None:
            id_, name_, email_, about_ = teacher_data
            return Teacher(id=id_, name=name_, email=email_, about=about_)


class SQLiteCourseMapper(SQLiteBaseMapper, CourseMapper):
    
    def __init__(self, connection):
        super().__init__(connection)
    
    def add(self, course: Course):
        
        teacher = SQLiteTeacherMapper(self.conn).get_by_name(name=course.teacher_name)
        if teacher is not None:
            sql = "INSERT INTO courses (id, name, type, teacherId) VALUES (?,?,?,?)"
            params = (None, course.name, course.type, teacher.id)
            self.execute(sql, params, commit=True)
    
    def get_course(self, by_type: str = None, by_teacher_name: str = None):
        sql = "SELECT courses.id, courses.name, courses.type, teachers.name " \
              "FROM courses JOIN teachers ON courses.teacherId = teachers.id;"
        params = ()
        if by_type is not None:
            sql = f'{sql} WHERE courses.type=?'
            params = by_type,
        elif by_teacher_name is not None:
            sql = f'{sql} WHERE courses.teacherId=?'
            teacher = SQLiteTeacherMapper(self.conn).get_by_name(name=by_teacher_name)
            if teacher is None:
                return
            params = teacher.id,
        output = []
        courses_data = self.execute(sql, params, fetchall=True)
        for id_, name_, type_, teacher_name_ in courses_data:
            output.append(Course(id=id_, name=name_, type=type_, teacher_name=teacher_name_))
        return output
