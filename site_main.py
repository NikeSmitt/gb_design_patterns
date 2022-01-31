import helper
from models import TrainingSite

training_site = TrainingSite()

for category in helper.categories:
    created_category = training_site.create_course_category(category)
    # print(created_category)
    training_site.categories.append(created_category)

for course in helper.courses:
    created_course = training_site.create_course(course)
    training_site.courses.append(created_course)
    
    # print(created_course)