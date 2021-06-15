from django import forms
from .models import BlgPost, BlgCategory

choices = BlgCategory.objects.all().values_list('name', 'name')


class BlgPostForm(forms.ModelForm):
    class Meta:
        model = BlgPost
        fields = ('title', 'title_tag', 'header_image', 'author', 'category', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'full-width',
            'placeholder': 'Your name'}),
            'title_tag': forms.TextInput(attrs={'class': 'full-width', 'placeholder': 'Title tag'}),
            'author': forms.Select(attrs={'class': 'ss-custom-select'}),
            'category': forms.Select(choices=list(choices), attrs={'class': 'full-width'}),
            'snippet': forms.Textarea(attrs={'class': 'message form-field full-width', 'placeholder': 'Short intro for your post.'}),
            'body': forms.Textarea(attrs={'class': 'message form-field full-width'}),
        }


class BlgEditForm(forms.ModelForm):
    class Meta:
        model = BlgPost
        fields = ('title', 'header_image', 'title_tag', 'category', 'snippet', 'body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'full-width'}),
            'title_tag': forms.TextInput(attrs={'class': 'full-width'}),
            'category': forms.Select(choices=list(choices), attrs={'class': 'full-width'}),
            'snippet': forms.Textarea(attrs={'class': 'message form-field full-width'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
