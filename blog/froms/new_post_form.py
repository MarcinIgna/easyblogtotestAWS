from blog.models.post_model import PostModel
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'author']