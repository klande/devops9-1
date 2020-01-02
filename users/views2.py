from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.

User = get_user_model()


def userlist(request, *args, **kwargs):
    users = User.objects.all()
    print(users)
    users_list = []
    for user in users:
        users_dict = {}
        users_dict['id'] = user.id
        users_dict['username'] = user.username
        users_dict['phone'] = user.phone
        users_list.append(users_dict)
        print(users_list)
    return HttpResponse(json.dumps(users_list), content_type="application/json")
