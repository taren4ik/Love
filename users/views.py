from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile

from profiles.models import User, Photo
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
        images = request.FILES.getlist('image')
        if form.is_valid():
            #user = form.save(commit=False)
            for f in images:
                data = f.read()  # Если файл целиком умещается в памяти
                photo = Photo(user=user)
                photo.image.save(f.name, ContentFile(data))
                photo.save()
            # for f in images:
            #     file_instance = User(image=f)
            #     print(file_instance)
            #     file_instance.save()
            # user.save()
            return redirect('profiles:profile_detail', request.user.pk)
    else:
        form = ChangeForm(instance=user)
    context = {
        "form": form,
        "user": user,
    }
    return render(request, 'users/profile_change_form.html', context)
