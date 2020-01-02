from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
# Create your views here.

User = get_user_model()


def userlist(request, *args, **kwargs):
    content = User.objects.all()
    print(type(content))
    print(content)
    return HttpResponse(content)
