from controllers.aboutPage import AboutPage
from controllers.indexPage import IndexPage

routes = {
    '/': IndexPage(),
    '/about': AboutPage()
}