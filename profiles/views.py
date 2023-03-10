import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

from .models import User, Comment, Category, Follow, Message, Photo
from .forms import CommentForm, MessageForm

COUNT_PROFILES = 10


def get_age(args):
    born = User.objects.get(id=args)
    age = datetime.datetime.now().year - born.year
    return age


def index(request):
    template = 'profiles/index.html'
    profile_list = User.objects.select_related("category")
    # images = Photo.objects.filter(user=request.user.pk)
    images = Photo.objects.all()
    paginator = Paginator(profile_list, COUNT_PROFILES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'images': images,
    }
    return render(request, template, context)


def category_profiles(request, slug):
    template = "profiles/profile_list.html"
    category = get_object_or_404(Category, slug=slug)
    paginator = Paginator(category.users.all(), COUNT_PROFILES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "category": category,
        "page_obj": page_obj,
    }
    return render(request, template, context)


def profile_detail(request, profile_id):
    template = 'profiles/profile_detail.html'
    profile = get_object_or_404(User.objects.select_related('category'),
                                id=profile_id)
    images = Photo.objects.filter(user=profile .pk)
    comments = Comment.objects.filter(profile_id=profile_id)
    age = get_age(profile_id)
    form = CommentForm(request.FILES or None)
    author = get_object_or_404(User, id=profile_id)
    following = False
    if request.user.is_authenticated and author != request.user:
        following = author.following.filter(user=request.user).exists()

    context = {
        "profile": profile,
        "form": form,
        'images': images,
        "comments": comments,
        'age': age,
        'following': following
    }

    return render(request, template, context)


@login_required
def profile_delete(request, profile_id):
    profile = User.objects.get(id=profile_id)
    profile.delete()
    return redirect("profiles:index")


@login_required
def add_comment(request, profile_id):
    """"Отправляет комментарий."""
    profile = get_object_or_404(User, id=profile_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.profile = profile
        comment.save()
    return redirect(profile)


@login_required
def send_message(request, profile_id):
    """"Отправляет сообщения."""
    template = "profiles/message.html"
    profile = get_object_or_404(User.objects.select_related('category'),
                                id=profile_id)
    messages = (Message.objects.filter(author=request.user, user=profile) |
                Message.objects.filter(author=profile,
                                       user=request.user)).order_by('id')
    form = MessageForm(request.POST or None)
    if form.is_valid():
        message = form.save(commit=False)
        message.author = request.user
        message.user = profile
        message.save()

    context = {
        "profile": profile,
        "form": form,
        "messages": messages
    }
    return render(request, template, context)


@login_required
def index_message(request):
    """"Вывод сообщений пользователя."""
    template = 'profiles/index_message.html'
    profile = get_object_or_404(User.objects.select_related('category'),
                                id=request.user.pk)
    messages = (Message.objects.filter(author_id=request.user.pk) |
                Message.objects.filter(user_id=request.user.pk)).order_by('id')
    context = {
        "messages": messages,
        "profile": profile,
    }
    return render(request, template, context)


@login_required
def follow_index(request):
    template = "profiles/follow.html"
    authors_ids = Follow.objects.filter(
        user=request.user).values_list('author_id', flat=True)  # input in list
    profiles = User.objects.filter(id__in=authors_ids)
    paginator = Paginator(profiles, COUNT_PROFILES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, template, context)


@login_required
def profile_follow(request, profile_id):
    author = get_object_or_404(User, id=profile_id)
    if author.id != request.user.pk:
        Follow.objects.get_or_create(user=request.user,
                                     author=author)
    return redirect("profiles:profile_detail", author.id)


@login_required
def profile_unfollow(request, profile_id):
    author = get_object_or_404(User, id=profile_id)
    user_follow = get_object_or_404(Follow.objects,
                                    user=request.user,
                                    author=author)
    user_follow.delete()
    return redirect("profiles:profile_detail", author.id)


def city(request):
    return HttpResponse(f'Город')
