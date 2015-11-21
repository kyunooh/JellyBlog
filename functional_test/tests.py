from django.test import LiveServerTestCase
from selenium import webdriver
from jellyblog.models import Category, Document


# 유저스토리 작성
class HomePageTest(LiveServerTestCase):
    
    def setUp(self):
        self.add_category_and_post()
        self.browser = webdriver.Firefox()
        self.browesr.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def add_category_and_post(self):
        Category.craete(parent=1, name="Home")
        Document.create(category=1, title="itemy 1 title",
                        content="itemy 1 content")
        Document.create(category=1, title="itemy 2 title",
                        content="itemy 2 content")
                        
        
    def test_visit_blog_home(self):
        # 브라우저를 통해 블로그 홈페이지에 접속한다. 
        self.browser.get(self.live_server_url)


