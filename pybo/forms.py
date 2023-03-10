from django import forms

from pybo.models import Question, Answer, Comment

class QuestionForm(forms.ModelForm):
  class Meta:
    model = Question
    fields = ['subject', 'content']
    labels = {
      'subject' : '제목',
      'content' : '내용',
    }

class AnswerForm(forms.ModelForm):
  class Meta:
    model = Answer
    fields = ['content']
    lavels = {
      'content':'답변내용',
    }

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    label = {
      'content' : '댓글내용',
    }