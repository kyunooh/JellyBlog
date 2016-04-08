import unittest
from selenium import webdriver
from about_me.models import Message


class MessageTest(unittest.TestCase):
    def setUp(self):
        self.test_name = 'functional test name'
        self.test_email = 'functional@test.email'
        self.test_content = 'functional test message content'

    def test_leave_message(self):
        # 유저는 메인 화면으로 들어와서
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000")
        self.assertIn('젤리의 망상', self.browser.title)
        # inform 을 클릭한다
        about_me_button = self.browser.find_element_by_css_selector('.box.inform')
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

        # 메시지를 남기고 브라우저 종료
        self.browser.quit()
