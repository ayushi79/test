from django import forms

class Blogform(forms.Form):
    title = forms.CharField(label = 'enter your title', max_length=100)
    blog = forms.CharField(widget=forms.Textarea)