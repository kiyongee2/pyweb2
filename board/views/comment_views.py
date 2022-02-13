from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from board.forms import CommentForm
from board.models import Comment, Question


@login_required(login_url='common:login')
def comment_create_question(request, question_id):
    # 질문 댓글 등록
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = CommentForm(request.POST)  #입력된 댓글 내용
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user  #세션 권한
            comment.create_date = timezone.now()
            comment.question = question   #참조 외래키
            comment.save()   # 실제 저장
            return redirect('board:detail', question_id=question.id)
    else: #GET은 빈 폼을 가져옴
        form = CommentForm()
    context = {'form':form}
    return render(request, 'board/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_question(request, comment_id):
    # 질문 댓글 삭제
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('board:detail', question_id=comment.question.id)

@login_required(login_url='common:login')
def comment_modify_question(request, comment_id):
    # 질문 댓글 수정
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment) #변경된 입력 내용
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('board:detail', question_id=comment.question.id)
    else:
        form = CommentForm(instance=comment)  # 채워진 폼
    context = {'form':form}
    return render(request, 'board/comment_form.html', context)