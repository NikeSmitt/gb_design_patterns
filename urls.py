from controllers.aboutPage import AboutPage
from controllers.contactsPage import ContactsPage
from controllers.indexPage import IndexPage

routes = {
    '/': IndexPage(),
    '/about': AboutPage(),
    '/contacts': ContactsPage(),
}