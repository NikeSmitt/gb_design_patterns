import helper
from database.db_main import db_handler
from models import TrainingSite, UserFactory

training_site = TrainingSite()

for category in helper.categories:
    created_category = training_site.create_course_category(category)
    # print(created_category)
    training_site.categories.append(created_category)

courses = db_handler.get_course()

for course in courses:
    name, type_, teacher_name = course
    # print(course)
    created_course = training_site.create_course({'name': name, 'type': type_, 'teacher_name': teacher_name})
    training_site.courses.append(created_course)

course = training_site.courses[0]

students = db_handler.get_all_students()
for student in students:
    name, email, about = student
    student_obj = UserFactory.create('student', name=name, email=email, about=about)
    training_site.add_user(student_obj)

course.add_student(training_site.students[0])
course.add_student(training_site.students[1])

# print(course.assign_students)
