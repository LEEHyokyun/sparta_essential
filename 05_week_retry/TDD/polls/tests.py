from django.test import TestCase

# Create your tests here.
class QuesionIndexViewTests(TestCase):
    def test_has_no_question(self):
        """
        If no any questions, message will be displayed.
        """
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "등록된 설문조사가 없습니다.")
        self.assertQuerysetEqual(response.context['question_list'], [])
