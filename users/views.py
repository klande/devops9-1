from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .serializers import UsersSerializer, GroupsSerializer
from django.contrib.auth.models import Group, Permission
from .serializers import PermissionSerializer, UsersCreateUpdateSerializer
# 导入分页模块
from rest_framework.pagination import PageNumberPagination
from utils.pagination import Pagination
# DRF自带过滤类
from rest_framework import filters
# 第三方过滤类
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins

User = get_user_model()


class UsersViewset(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer


class UsersCreateUpdateViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersCreateUpdateSerializer


class GroupsViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer


# class PageNumber(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'page_size'
#     page_query_param = 'page'
#     max_page_size = 10


class PermissionsViewset(viewsets.ReadOnlyModelViewSet):
    """
    list:
    返回permission列表
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_field = ['name', 'codename']
    ordering_fields = ['id', ]
