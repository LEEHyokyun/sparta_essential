from django.test import TestCase
from django.utils import timezone
from .models import Question, Choice
import datetime

def create_question(question_text, time_delta_from_now):
    """
    Create a question with parameters
    """

    time = timezone.now() + time_delta_from_now
    question = Question(question_text = question_text, pub_date = time)
    question.save()

    return question

# Create your tests here.
class QuesionIndexViewTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False when Question date is in the future
        """
        time = timezone.now() - datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False when Question date is in the past, over 1 days
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True when Question date is in the past, less 1 days
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)

    def test_has_no_question(self):
        """
        If no any questions, message will be displayed.
        """
        response = self.client.get("/polls/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "등록된 설문조사가 없습니다.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_published_recently_has_new_mark(self):
        """
        Questions with a recent pub_date are displayed
        with <New> marked
        """

        question = create_question("test", datetime.timedelta(hours=-8))
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "[New]")
        self.assertQuerysetEqual(response.context['question_list'], [question])

    def test_past_question(self):
        """
        Questions in the past would be displayed
        """
        question = create_question("test", datetime.timedelta(days=-30))
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], [question])

    def test_future_question(self):
        """
        Questions in the past would be displayed
        """
        question = create_question("test", datetime.timedelta(days=30))
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "등록된 설문조사가 없습니다.")
        self.assertQuerysetEqual(response.context['question_list'], [])

    def test_two_past_questions(self):
        """
        Questions would be displayed with sorted by pub_date
        """
        question1 = create_question("test", datetime.timedelta(days=-30))
        question2 = create_question("test", datetime.timedelta(days=-5))
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['question_list'], [question2, question1])