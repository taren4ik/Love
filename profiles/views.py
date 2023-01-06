from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

from .models import User, Category, Follow


def profile_detail(request, profole_id):
    return HttpResponse(f'Профайл {profole_id}')


def profile(request):
    return HttpResponse('Профайл ')


def city(request):
    return HttpResponse(f'Город')
