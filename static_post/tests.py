from django.core.urlresolvers import reverse
from django.test.testcases import LiveServerTestCase

from selenium import webdriver


class DjangoGirlsJulySeminarViewTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_get_slide(self):
        self.browser.implicitly_wait(3)
        self.browser.get(self.live_server_url + reverse("django_girls_july_seminar"))
        elem = self.browser.find_element_by_xpath("//*")
        index_html = elem.get_attribute("outerHTML")


        self.assertIn("HTML과 CSS의 기본과 활용", self.browser.title)
        self.assertIn("감사합니다.", index_html)