from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=100)  #제목 칼럼
    content = models.TextField()                #질문 내용
    create_date = models.DateTimeField()        #질문 작성일
    modify_date = models.DateTimeField(null=True, blank=True)  #질문 수정일
    voter = models.ManyToManyField(User, related_name='voter_question')   #추천수(다대다관계)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키, 제목
    content = models.TextField()          #답변 내용
    create_date = models.DateTimeField()  #답변 작성일
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.content

# Comment 모델 생성
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #댓글 글쓴이
    content = models.TextField()          #댓글 내용
    create_date = models.DateTimeField()  #작성일
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, # 질문 댓글
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True,     # 답변 댓글
                                 on_delete=models.CASCADE)

