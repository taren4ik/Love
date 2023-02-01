from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model

from .forms import CreationForm, ChangeForm

User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("profiles:index")
    template_name = "users/signup.html"


def ProfileChange(request):
    user = get_object_or_404(User, pk=request.user.pk)

    if user.pk != request.user.pk:
        return redirect("profiles:profile_detail", request.user.pk)
    if request.method == "POST":
        form = ChangeForm(
            request.POST or None,
            files=request.FILES or None,
            instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('profiles:profile_detail', request.user.pk)
    else:
        form = ChangeForm(instance=user)
    context = {
        "form": form,
        "user": user,
    }
    return render(request, 'users/profile_change_form.html',   context)
