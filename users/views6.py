from django.core import serializers
import json
from django.http import JsonResponse, QueryDict
from django.contrib.auth import get_user_model
from django.views.generic import View, ListView, DetailView

User = get_user_model()


# Create your views here.
class UsersListView(View):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        users_list = serializers.serialize('json', users)
        users_list = json.loads(users_list)
        return JsonResponse(users_list, safe=False)

    def post(self, request, *args, **kwargs):
        print(request.body)  # b'{"username=wd&age=18"}'
        print(request.POST)  # <QueryDict: {'{"username': ['wd'], 'age': ['18"}']}>
        print(dict(request.POST))  # {'{"username': ['wd'], 'age': ['18"}']}
        print(type(dict(request.POST)))  # <class 'dict'>
        res = {'code': 0, "result": "pust is ok"}
        return JsonResponse(res, safe=True)

    def delete(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(request.body)  # b'{"username=wd&age=18"}'
        data = QueryDict(request.body).dict()
        print(data)  # {'{"username': 'wd', 'age': '18"}'}
        res = {'code': 0, "result": "put is ok"}
        return JsonResponse(res, safe=True)

    def patch(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
