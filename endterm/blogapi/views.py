from django.shortcuts import render
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

@csrf_exempt
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        posts_json = [t.to_json() for t in posts]
        return JsonResponse(posts_json, safe=False)
      
    elif request.method == "POST":
        data = request.POST
        post = Post()
        post.title = data.get('title','')
        post.text = data.get('text','')
        post.save()
    
    return JsonResponse(post.to_json(), safe=False)
       
    
def post_details(request, post_id):
    post = Post.objects.get(pk=post_id)
    return render(request, 'blog/post_details.html', {'post': post})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('post_list')
