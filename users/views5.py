from django.core import serializers
import json
from django.http import JsonResponse, QueryDict
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


def userlist(request, *args, **kwargs):
    if request.method == "GET":
        users = User.objects.all()
        print("queryset\n {}".format(users))
        users_list = serializers.serialize('json', users)
        print("serializers\n {}".format(users_list))
        users_list = json.loads(users_list)
        print("json_load\n {}".format(users_list))
        return JsonResponse(users_list, safe=False)
    elif request.method == "POST":
        print(request.body)  # b'{"username=wd&age=18"}'
        print(request.POST)  # <QueryDict: {'{"username': ['wd'], 'age': ['18"}']}>
        print(dict(request.POST))  # {'{"username': ['wd'], 'age': ['18"}']}
        print(type(dict(request.POST)))  # <class 'dict'>
        res = {'code': 0, "result": "pust is ok"}
        return JsonResponse(res, safe=True)
    elif request.method == "PUT":
        print(request.body)  # b'{"username=wd&age=18"}'
        data = QueryDict(request.body).dict()
        print(data)  # {'{"username': 'wd', 'age': '18"}'}
        res = {'code': 0, "result": "put is ok"}
        return JsonResponse(res, safe=True)
    elif request.method == "DELETE":
        print(request.body)  # b'{"username=wd&age=18"}'
        data = QueryDict(request.body).dict()
        print(data)  # {'{"username': 'wd', 'age': '18"}'}
        res = {'code': 0, "result": "delete is ok"}
        return JsonResponse(res, safe=True)
