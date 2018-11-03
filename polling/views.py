from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse

#from django.template import loader

#def index(request):
#    qustn_list= Question.objects.order_by("-pub_date")
#    template = loader.get_template('polling/index.html')
#    context = {'qustn_list':qustn_list}
#    return HttpResponse(template.render(context,request))

def index(request):
    qustn_list = Question.objects.order_by("-pub_date")
    return render(request,'polling/index.html',{'qustn_list':qustn_list})

#def detail(request,question_id):
 #   try:
  #      q = Question.objects.get(pk=question_id)
   #     template = loader.get_template('polling/detail.html')
    #    context = {'q': q}
    #except Question.DoesNotExist:
     #   raise Http404("Question Does not Exist")
    #return HttpResponse(template.render(context, request))

def detail(request, question_id):
    q= get_object_or_404(Question, pk=question_id)
    return render(request,'polling/detail.html',{'q':q})

def vote(request,question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polling/detail.html', {'q':q, 'error_msg': "you didn't select a choice"})
    else:
        selected_choice.votes+=1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polling:results', args=(q.id,)))

def results(request,question_id):
    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polling/result.html', {'q': q})



