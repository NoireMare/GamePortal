from django import forms
from .models import Post, Comment, User
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=CKEditorUploadingWidget(attrs={
        'rows': 30, 'cols': 100}))

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']


class EditPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput())
    text = forms.CharField(widget=CKEditorUploadingWidget(attrs={
        'rows': 30, 'cols': 100}))

    class Meta:
        model = Post
        fields = ['title', 'text', 'image', 'category']


class AddCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 5, 'cols': 100, 'placeholder': 'Write your comment here...'}))

    class Meta:
        model = Comment
        fields = ['text']





