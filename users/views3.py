from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.forms.models import model_to_dict
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

User = get_user_model()


def userlist(request, *args, **kwargs):
    users = User.objects.all()
    users_list = []
    for user in users:
        users_dict = model_to_dict(user)
        # model_to_dict 可以吧查出来的信息直接转成字典
        # users_dict['last_login'] = str(users_dict['last_login'])
        # users_dict['date_joined'] = str(users_dict['date_joined'])
        # del users_dict['groups']
        # del users_dict['user_permissions']
        users_list.append(users_dict)
    print(users_list)
    return JsonResponse(users_list, safe=False)
