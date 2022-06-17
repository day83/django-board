from django import forms

from .models import Post

class NewPostForm(forms.Form):
    title = forms.CharField(max_length=200)
    user_name = forms.CharField(max_length=50, required=False, label='User', widget=forms.TextInput(attrs = {'placeholder': 'Optional'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs = {'placeholder': 'Optional'}))
    content = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'Message'}), label='')
    image = forms.ImageField()

class NewCommentForm(forms.Form):
    title = forms.CharField(max_length=200, required=False, widget=forms.TextInput(attrs = {'placeholder': 'Optional'}))
    user_name = forms.CharField(max_length=50, required=False, label='User', widget=forms.TextInput(attrs = {'placeholder': 'Optional'}))
    email = forms.EmailField(required=False, widget=forms.TextInput(attrs = {'placeholder': 'Optional'}))
    content = forms.CharField(widget=forms.Textarea(attrs = {'placeholder': 'Message'}), label='')
    image = forms.ImageField(required=False, label='Image (optional)')
