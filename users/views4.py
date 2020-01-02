from django.core import serializers
import json
from django.http import JsonResponse
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()


def userlist(request, *args, **kwargs):
    users = User.objects.all()
    users_list = serializers.serialize('json', users)
    print(users_list)
    print(type(users_list))
    users_list = json.loads(users_list)
    print(type(users_list))
    return JsonResponse(users_list, safe=False)
