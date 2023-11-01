from django import forms

class CommentsForm(forms.Form):
    post_id = forms.IntegerField()
    text = forms.CharField()
