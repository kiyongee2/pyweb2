from django.shortcuts import render
from polls.models import Question, Choice

def index(request):
    #설문 메인
    question_list = Question.objects.all()
    context = {'question_list':question_list}
    return render(request, 'polls/poll_list.html', context)

def detail(request, pk):
    #설문 상세
    # question = Question.objects.get(id=pk)
    question = Question.objects.get(id=pk)
    context = {'question':question}
    return render(request, 'polls/poll_detail.html', context)

def vote(request, pk):
    #투표하기
    question = Question.objects.get(id=pk)
    try:
        choice = request.POST['choice']  #선택한 내용
        sel_choice = question.choice_set.get(id=choice)
    except:
        context = {'question':question, 'error':'선택을 확인하세요!'}
        return render(request, 'polls/poll_detail.html', context)
    else:
        sel_choice.votes += 1 #1 더하기
        sel_choice.save()     #저장
        context = {'question':question}
        return render(request, 'polls/poll_result.html', context)
