from django.test.testcases import LiveServerTestCase
from selenium import webdriver

from about_me.models import Message
from jellyblog.models import Category, Document
from jellyblog.views import init_category


class MessageTest(LiveServerTestCase):
    def setUp(self):
        # 유저는 메인 화면으로 들어와서
        self.browser = webdriver.Firefox()
        self.test_name = 'functional test name'
        self.test_email = 'functional@test.email'
        self.test_content = 'functional test message content'

    def tearDown(self):
        self.browser.quit()

    def test_leave_message(self):
        self.browser.get(self.live_server_url)
        self.assertIn('젤리의 망상', self.browser.title)
        # inform 을 클릭한다
        about_me_button = self.browser.find_element_by_css_selector(
            '.box.inform')
        # 클릭이후 about_me 페이지로 이동한다.
        about_me_button.click()
        self.assertIn('젤리의 망상 - About me', self.browser.title)
        # Message Form을 확인 후 메시지를 남긴다.
        name = self.browser.find_element_by_name('name')
        name.send_keys(self.test_name)

        email = self.browser.find_element_by_name('email')
        email.send_keys(self.test_email)

        content = self.browser.find_element_by_name('content')
        content.send_keys(self.test_content)

        self.browser.find_element_by_tag_name('form').submit()
        # Message가 서버에 저장된다.
        # 다시 about me page로 돌아온다.
        self.assertIn('젤리의 망상 - About me', self.browser.title)

        ## Message가 저장되었는지 확인
        message = Message.objects.get(
            name=self.test_name,
            email=self.test_email,
            content=self.test_content
        )
        self.assertTrue(message)


class SearchTest(LiveServerTestCase):
    def setUp(self):
        init_category()
        category = Category.objects.get(name="Home")
        self.searchTestDoc1 = Document.objects.create(
            category=category,
            title="Document Search Test Document",
            content="Search Document Content1 It Would Be Found",
            meta_tag="searchsearchesarchesarchsearch",
            public_doc=True
        )

        self.notFoundDoc1 = Document.objects.create(
            category=category,
            title="Not Found Document",
            content="Search Document Content1 It Would Be Found",
            meta_tag="searchsearchesarchesarchsearch",
            public_doc=False
        )

        self.notFoundDoc2 = Document.objects.create(
            category=category,
            title="Not found",
            content="This Content is not found",
            meta_tag="notnotnotnotnot foundounfdouynfdounfdounfd",
            public_doc=True
        )
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_search_doc(self):
        self.browser.get(self.live_server_url)
        blog_button = self.browser.find_element_by_css_selector(
            '.box.blog_link')
        blog_button.click()
        self.assertIn("젤리의 망상", self.browser.title)

        search_box = self.browser.find_element_by_id("search_query")
        search_box.send_keys("It Would Be Found")

        search_button = self.browser.find_element_by_id("search_box")
        search_button.click()

        elem = self.browser.find_element_by_xpath("//*")
        index_html = elem.get_attribute("outerHTML")

        self.assertIn(self.searchTestDoc1.title, index_html)
        self.assertNotIn(self.notFoundDoc1.title, index_html)
        self.assertNotIn(self.notFoundDoc2.title, index_html)
