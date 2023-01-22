import datetime
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

from .models import User, Comment, Category, Follow
from .forms import CommentForm

COUNT_PROFILES = 10


def get_age(args):
    born = User.objects.get(id=args)
    age = datetime.datetime.now().year - born.year
    return age


def index(request):
    template = 'profiles/index.html'
    profile_list = User.objects.select_related("category")
    paginator = Paginator(profile_list, COUNT_PROFILES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(paginator)
    context = {
        "page_obj": page_obj,
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
    comments = Comment.objects.filter(profile_id=profile_id)
    age = get_age(profile_id)
    form = CommentForm(request.FILES or None)
    context = {
        "profile": profile,
        "form": form,
        "comments": comments,
        'age': age,
    }

    return render(request, template, context)


@login_required
def profile_delete(request, profile_id):
    profile = User.objects.get(id=profile_id)
    profile.delete()
    return redirect("profiles:index", username=request.user)


@login_required
def add_comment(request, profile_id):
    profile = get_object_or_404(User, id=profile_id)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.profile = profile
        comment.save()
    return redirect(profile)


@login_required
def follow_index(request):
    template = "profile/follow.html"
    authors_ids = Follow.objects.filter(
        user=request.user).values_list('author_id', flat=True)  # input in list
    profiles = User.objects.filter(author_id__in=authors_ids)
    print(profiles)
    paginator = Paginator(profiles, COUNT_PROFILES)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, template, context)


@login_required
def profile_follow(request, username):
    print(username)
    author = get_object_or_404(User, username=username)
    if author != request.user:
        Follow.objects.get_or_create(user=request.user, author=author)
    return redirect("profiles:profile_detail", author)


@login_required
def profile_unfollow(request, username):
    author = get_object_or_404(User, username=username)
    user_follow = get_object_or_404(Follow.objects,
                                    user=request.user,
                                    author=author)
    user_follow.delete()
    return redirect("profiles:profile_detail", author)


def city(request):
    return HttpResponse(f'Город')
