#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from .models import User, Feedback
from itreactor.settings import STATIC_URL, PROFILE_PHOTO_DEFAULT_NAME, PROFILE_PHOTOS_DIR


class RegisterView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'


# Create your views here.
@csrf_protect
def get_photo(request, username):
    # Тут код отдачи фотографии
    try:
        user = User.objects.get(username=username)
        photo = user.get_photo().path
    except:
        return redirect(os.path.join(PROFILE_PHOTOS_DIR, PROFILE_PHOTO_DEFAULT_NAME))

    # print(os.path.join(PROFILE_PHOTOS_DIR, photo))
    return redirect(os.path.join(STATIC_URL, PROFILE_PHOTOS_DIR + photo))


@csrf_protect
def feedback(request):
    message = Feedback.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        subject=request.POST['subject'],
        message=request.POST['message'],
    )
    message.save()
    # Отправка письм
    user = User.objects.get(is_superuser=True)
    user.send_email(name=message.name, from_email=message.email, subject=message.subject, message=message.message)
    return JsonResponse(True, safe=False)
