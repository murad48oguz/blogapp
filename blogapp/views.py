from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from blogapp.models import *

from .forms import CommentForm


@login_required(login_url='login')
def home(request):
    # posts = Post.objects.all()
    context = {
        "posts" : Post.objects.all()
    }
    return render(request,'index.html',context)
    
    
    # context = dict()                       #her iki context istifadesi de dogrudur. 
    # context['posts'] = Post.objects.all()
    # return render(request,'index.html',context)


def post_detail(request,id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.save()
            
            return redirect('post_detail', id = post.id)
    else:
        form = CommentForm()
    
    
    context = {
        'post': post,
        'form': form
    }
    return render(request,'post_detail.html',context)


def loginpage(request): 
    
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
    
        if request.method == "POST":
            username= request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect ('home')
            else:
                messages.info(request, "USERNAME or PASSWORD is incorrect")
            
        return render(request,'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')
    


def register(request):
    
    if request.user.is_authenticated:
        return redirect('home')
    
    else:
        form = UserCreationForm()
        
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Account has been created for " + user )
                return redirect('login')
                
            
            
        context = {"form": form}
        return render(request,'register.html', context)
    
    
def tag(request, a):
    tags=Tag.objects.get(id=a)
    # print(tags)
    
    post=Post.objects.filter(tag=tags)
    # print(post)
    
    context = {
        'tag':tags.post_set.all(),
        'post':post
        
     }
    
    return render(request,"tag.html",context)
