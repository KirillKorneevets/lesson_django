from django import forms

class PostsForm(forms.Form):
    post = forms.CharField(min_length=5, max_length=100)
    text = forms.CharField(min_length=10, max_length=500)
