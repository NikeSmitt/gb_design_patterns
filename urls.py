from controllers.aboutPage import AboutPage
from controllers.categoryPage import CategoriesPage
from controllers.contactsPage import ContactsPage
from controllers.coursesPage import CoursesPage
from controllers.indexPage import IndexPage

routes = {
    '/': IndexPage(),
    '/about': AboutPage(),
    '/contacts': ContactsPage(),
    '/categories': CategoriesPage(),
    '/courses': CoursesPage()
}