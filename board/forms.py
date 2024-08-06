from django import forms
from .models import Post


# class PostForm(forms.Form):
#     author = forms.CharField(max_length=50, label='Автор')
#     title = forms.CharField(max_length=200, label='Заголовок')
#     text = forms.CharField(label='Текст объявления', widget=forms.Textarea)

# второй способ создания форм более простой
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'text', 'image', 'url_adders']  # так правильнее всего
        # второй способ не надо так делать
        # fields = '__all__'
        # exclude = ['created_at'] или так


# class DeleteNewForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = []
