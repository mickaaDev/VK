from django import forms
from .models import * 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]

class CommentToCommentForm(forms.ModelForm):
    class Meta:
        models = Comment_to_comment
        fields = ["text"]
