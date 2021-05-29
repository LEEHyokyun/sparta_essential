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

    def test_has_a_href_link(self):
        """
        Questions would be displayed with a href link
        """
        question = create_question("test", datetime.timedelta(days=-30))
        response = self.client.get("/polls/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, f'href="/polls/{question.id}/')

class  QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        questions in the future would return 404 not found page
        """
        future_question = create_question(question_text="test", time_delta_from_now=datetime.timedelta(days=5))
        response = self.client.get(f"/polls/{future_question.id}/")
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        questions in the past would return each question_text
        """
        past_question = create_question(question_text="test", time_delta_from_now=datetime.timedelta(days=-5))
        response = self.client.get(f"/polls/{past_question.id}/")

    def test_past_question_with_choices(self):
        """
        question in the past would return the question's choice
        """
        past_question = create_question(question_text="test", time_delta_from_now=datetime.timedelta(days=-5))

        choice1 = Choice(question=past_question, choice_text="choice 1")
        choice1.save()
        choice2 = Choice(question=past_question, choice_text="choice 2")
        choice2.save()

        response = self.client.get(f"/polls/{past_question.id}/")

        self.assertContains(response, choice1.choice_text)
        self.assertContains(response, choice2.choice_text)


#1. 질문 리스트페이지에서 질문 개별 페이지로 이동할 수 있는 href 링크를 제공해야 합니다.
#2. 현재 발행되지 않은 질문의 디테일 뷰에 접속했을 때 404 에러가 나와야 합니다.
#3. 이미 발행된 질문에 접속하면 해당 질문의 내용이 존재해야 합니다.
#4. 이미 발행된 질문에 접속하면 해당 질문에 대한 선택들 내용도 존재해야 합니다.