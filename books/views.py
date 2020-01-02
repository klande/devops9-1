from django.shortcuts import render

from rest_framework import viewsets
# drf自带的分页
from rest_framework.pagination import PageNumberPagination
# drf 自带的过滤器，提供了SearchFilter，OrderingFilter搜索和排序功能
from rest_framework import filters
# 第三方过滤器，高度可定制，DjangoFilterBackend 默认是精确（查找）过滤，即字段值必需要完全一样才能匹配成功
from django_filters.rest_framework import DjangoFilterBackend
# drf 自带的三种用户认证方式
from rest_framework.authentication import TokenAuthentication, BaseAuthentication, SessionAuthentication
# jwt用户认证方式
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

# drf自带的权限管理系统
from rest_framework.permissions import IsAuthenticated

# 引入自定义的模型、序列化、过滤器类
from .models import Publish, Author, Book
from .serializers import PublishSerializer, AuthorSerializer, BookSerializer


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100


class PublishViewSet(viewsets.ModelViewSet):
    """
    list:
      列出所有出版商
    retrieve:
      某个出版商的详细信息
    create:
      创建出版商
    update:
      更新出版商
    delete:
      删除出版商
    """

    # 查询结果集
    queryset = Publish.objects.all()
    # 调用序列化类
    serializer_class = PublishSerializer
    # 调用分页类
    pagination_class = Pagination


class AuthorViewSet(viewsets.ModelViewSet):
    """
    list:
      列出所有出版商
    retrieve:
      某个出版商的详细信息
    create:
      创建出版商
    update:
      更新出版商
    delete:
      删除出版商
    """

    # 查询结果集
    queryset = Author.objects.all()
    # 调用序列化类
    serializer_class = AuthorSerializer
    # 调用分页类
    pagination_class = Pagination


class BookViewSet(viewsets.ModelViewSet):
    # 查询结果集
    queryset = Book.objects.all()
    # 调用序列化类
    serializer_class = BookSerializer
    # 调用分页类
    pagination_class = Pagination
    # drf 自带的过滤器
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    # 'publisher__name' 可以搜索外键中的字段
    search_fields = ('name', 'publisher__name', "authors__name")
    # 排序 按照某个字段进行排序
    ordering_fields = ('publication_date', )
