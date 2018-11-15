from django.urls import path
from . import views

app_name= 'polling'

#urlpatterns = [
#    path('',views.index, name='index'),
#    path('<int:question_id>/',views.detail, name='detail'),
#    path('<int:question_id>/vote/',views.vote, name='vote'),
#    path('<int:question_id>/results/',views.results, name='results'),
#]

urlpatterns[
   path('',views.IndexView.as_view(), name='index'),
   path('<int:pk>/',views.DetailView.as_view(), name='detail'),
   path('<int:question_id>/vote/',views.votes, name='vote'),
   path('<int:pk>/results/',views.ResultsView.as_view(), name='results'), 
]
