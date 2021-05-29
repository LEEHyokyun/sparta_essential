from django.db import models
from django.utils import timezone
import datetime


# Create your models here.
class Question(models.Model):
    # 문자열 저장
    question_text = models.CharField(max_length=200)
    # 질문발행시간
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    # 투표수
    votes = models.IntegerField(default=0)
