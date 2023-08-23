from django.http import HttpResponse
from blog.models.post_model import PostModel
from blog.froms.new_post_form import PostForm
from django.shortcuts import render, redirect

class PostView:
    def new_post(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('blog:main')
        else:
            form = PostForm()
        return render(request, 'new_post_form.html', {'form': form})