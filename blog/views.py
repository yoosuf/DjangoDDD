from django.shortcuts import render, redirect
from .services.post_service import PostService
from .services.category_service import CategoryService
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist

post_service = PostService()
category_service = CategoryService()

def home(request):
    posts = post_service.list_posts()
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, post_id):
    try:
        post = post_service.get_post_by_id(post_id)
    except ObjectDoesNotExist:
        return render(request, '404.html', status=404)
    return render(request, 'post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_service.create_post(
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                author=request.user,
                category=form.cleaned_data['category']
            )
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_service.create_category(name)
        return redirect('home')
    return render(request, 'create_category.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')