from django.shortcuts import render
from blog.models.post_model import PostModel

def main(request):
    return render(request, 'main.html', {'posts': PostModel.objects.all()})