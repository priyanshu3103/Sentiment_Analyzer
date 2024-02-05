from django import forms

class SentimentForm(forms.Form):
    text_input = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}))
