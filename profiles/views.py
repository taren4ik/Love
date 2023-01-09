from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

from .models import User, Comment, Category, Follow
from  .forms import CommentForm

COUNT_POSTS = 10


# def profile_detail(request, profile_id):
#     template = "profiles/index.html"
#     return render(request, template)

def index(request):
    template = "posts/index.html"
    profile_list = User.objects.select_related("category")
    paginator = Paginator(profile_list, COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
    }
    return render(request, template, context)


def profile_detail(request, profile_id):
    template = "profiles/profile_detail.html"
    post = get_object_or_404(User.objects.select_related("author"),
                             id=profile_id)
    comments = Comment.objects.filter(profile_id=profile_id)
    form = CommentForm(request.user or None)
    context = {
        "profile": profile,
        "form": form,
        "comments": comments,
    }
    return render(request, template, context)


def profile(request):
    return HttpResponse('Профайл ')


@login_required
def follow_index(request):
    template = "profile/follow.html"
    authors_ids = Follow.objects.filter(
        user=request.user).values_list('author_id', flat=True)
    posts = User.objects.filter(author_id__in=authors_ids)
    paginator = Paginator(posts, COUNT_POSTS)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
    }
    return render(request, template, context)


def city(request):
    return HttpResponse(f'Город')
