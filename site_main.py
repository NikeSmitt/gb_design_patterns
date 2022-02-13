import helper
from database.db_main import student_mapper, teacher_mapper, course_mapper
from models import TrainingSite, UserFactory

training_site = TrainingSite()

for category in helper.categories:
    created_category = training_site.create_course_category(category)
    # print(created_category)
    training_site.categories.append(created_category)

courses = course_mapper.get_course()

for course in courses:
    training_site.courses.append(course)

course = training_site.courses[0]

students = student_mapper.get_all()
for student in students:
    training_site.add_user(student)

course.add_student(training_site.students[0])
course.add_student(training_site.students[1])
course.subscribe(training_site.students[0])
course.subscribe(training_site.students[1])

# print(course.assign_students)
