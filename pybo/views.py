from django.shortcuts import render
from django.http import HttpResponse
from . import models
from .models import Question
from django.shortcuts import get_object_or_404


# Create your views here.

def index(request):
    question_list = Question.objects.order_by('-created_date')
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'pybo/question_detail.html', context)


