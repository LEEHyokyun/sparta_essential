from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.utils import timezone
# Create your views here.

def index(request):
    question_list = Question.objects.all().filter(
        pub_date__lte = timezone.now()
    ).order_by('-pub_date')
    #output = ', '.join([q.question_text for q in question_list])

    context = {
        'question_list' : question_list
    }

    return render(request, 'polls/index.html', context)