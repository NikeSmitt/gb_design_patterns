import helper
from helper import students
from models import TrainingSite, UserFactory

training_site = TrainingSite()

for category in helper.categories:
    created_category = training_site.create_course_category(category)
    # print(created_category)
    training_site.categories.append(created_category)

for course in helper.courses:
    created_course = training_site.create_course(course)
    training_site.courses.append(created_course)


course = training_site.courses[0]
# print(course)

for user in students:
    new_user = UserFactory.create('student', **user)
    course.add_student(new_user)
    
# print(course.assign_students)
