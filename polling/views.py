#from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Question,Choice
from django.template import loader

def index(request):
    qustn_list= Question.objects.order_by("-pub_date")
    template = loader.get_template('polling/index.html')
    context = {'qustn_list':qustn_list}
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        q = Question.objects.get(pk=question_id)
        template = loader.get_template('polling/detail.html')
        context = {'q': q}
    except Question.DoesNotExist:
        raise Http404("Question Does not Exist")
    return HttpResponse(template.render(context, request))

def vote(request,question_id):
    return HttpResponse("Vote for Question: %s" %question_id)

def results(request,question_id):
    return HttpResponse("Results to the voting can be seen here")



