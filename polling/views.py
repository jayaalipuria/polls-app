#from django.shortcuts import render

from django.http import HttpResponse
from .models import Question,Choice
from django.template import loader

def index(request):
    qustn_list= Question.objects.order_by("-pub_date")
    template = loader.get_template('polling/index.html')
    context = {'qustn_list':qustn_list}
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse("You are at Question: %s"%q.question_txt)

def vote(request,question_id):
    return HttpResponse("Vote for Question: %s" %question_id)

def results(request,question_id):
    return HttpResponse("Results to the voting can be seen here")



