from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView
from .models import Post, PostComment
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseNotFound, Http404
from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User, auth



# Create your views here.
def postdetail(request, cid):
    post = Post.objects.get(pk=cid)
    comments = PostComment.objects.all().filter(post = post)
    data = {"post" : post , "comments" : comments}

    return render(request,'postpage.html',data)

def userdetail(request, cid):
    user = User.objects.get(pk=cid)
    data = {"user" : user }
    return render(request,'userpage,html',data)
 
    
def home(request):
    posts = Post.objects.all()
    data = {"posts" : posts }
    for i in posts:
        print(i.title)
    return render(request, 'home.html',data)

# def search(request):
#    query = request.GET.get('q')
#    if query:
#       posts = Post.objects.filter(Q(title__icontains=query) | Q(body__icontains=query)).order_by('-post_date')
#    else:
#       posts = Post.objects.all()
   
# #    cat_list = Categories.objects.all()
# #    latestpost_list = Post.objects.all().order_by('-post_date')[:3]
# #    paginator = Paginator(posts, 2)
# #    page = request.GET.get('page')
# #    posts = paginator.get_page(page)
#    data = {'posts':posts , 'query':query}

#    return render(request,'search_list.html', data)

def blog(request):
    return redirect('/')


def create_comment(request, cid):
    print("create works")
    post = Post.objects.get(pk=cid)
    data = { "post" : post}
    return render(request,"create_comment.html",data)


def save_comment(request, cid):
    print("save works")
    print(cid)
    
    if request.user.is_authenticated:
        body = request.POST.get('body')
        post = Post.objects.get(pk=cid)
        comments = PostComment.objects.all().filter(post = post)
        data = {"post" : post , "comments" : comments}
        comment = PostComment(user = request.user,post = post ,body = body)
        comment.save()
        return redirect(postdetail,cid)
    else:
        return redirect('login')