from django.urls import path
from .views import QuestionList,AnswerList
from SaeAudition import views
app_name='SaeAudition'

urlpatterns = [
    path('',QuestionList.as_view(), name='queslist'),
    path('answer/',AnswerList.as_view({'get': 'list'}),name='answerlist'),
]
