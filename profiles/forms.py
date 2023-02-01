from django import forms

from .models import Comment, Message


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)


class MessageForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("text",)
