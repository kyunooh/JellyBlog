from django.test import LiveServerTestCase


class MessageTest(LiveServerTestCase):
    def leave_message(self):
        # 유저는 메인 화면으로 들어와서
        # inform 을 클릭한다

        # 클릭이후 about_me 페이지로 이동한다.

        # Message Form을 확인 후 메시지를 남긴다.

        # Message가 서버에 저장된다.