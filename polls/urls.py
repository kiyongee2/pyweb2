from django.urls import path
from polls import views

app_name = 'poll'

urlpatterns = [
    #설문 조사 메인 - 127.0.0.1:8000/polls
    path('', views.index, name='index'),
    # 설문 상세
    path('<int:pk>/', views.detail, name='detail'),
    # 설문 투표
    path('<int:pk>/vote/', views.vote, name='vote')
]