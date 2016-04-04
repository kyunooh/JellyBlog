import unittest
from selenium import webdriver


class MessageTest(unittest.TestCase):
    def test_leave_message(self):
        # 유저는 메인 화면으로 들어와서
        self.browser = webdriver.Firefox()
        self.browser.get("http://localhost:8000")
        self.assertIn('젤리의 망상', self.browser.title)
        # inform 을 클릭한다
        about_me_button = self.browser.find_element_by_id('about_me')
        # 클릭이후 about_me 페이지로 이동한다.
        about_me_button.click()
        self.assertIn('젤리의 망상 - About me', self.browser.title)
        # Message Form을 확인 후 메시지를 남긴다.

        # Message가 서버에 저장된다.

        # 메시지를 남기고 브라우저 종료
        self.browser.quit()
