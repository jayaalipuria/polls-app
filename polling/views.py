from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question,Choice
from django.urls import reverse
from django.views import generic

#def index(request):
#    qustn_list = Question.objects.order_by("-pub_date")
#    return render(request,'polling/index.html',{'qustn_list':qustn_list})

class IndexView(generic.ListView):
    template_name = 'polling/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
#def detail(request, question_id):
#    q= get_object_or_404(Question, pk=question_id)
 #   return render(request,'polling/detail.html',{'q':q})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polling/detail.html'
    
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

#def results(request,question_id):
  #  q = get_object_or_404(Question, pk=question_id)
  #  return render(request, 'polling/result.html', {'q': q})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polling/result.html'
