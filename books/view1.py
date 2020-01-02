from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers2 import PublishSerializer
from .models import Publish
from django.http import Http404


# 版本一 APIView + serializer


class PublishList(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Publish.objects.all()
        publish_list = PublishSerializer(queryset, many=True)
        return Response(publish_list.data)

    def post(self, request, *args, **kwargs):
        data = request.data
        publish = PublishSerializer(data=data)
        print(publish)
        if publish.is_valid():
            print("1111")
            publish.save()
            return Response(publish.data, status=200)
        return Response(publish.data, status=400)


class PublishDetail(APIView):

    def get_object(self, pk):

        try:
            return Publish.objects.get(pk=pk)
        except Publish.DoesNotExist:
            raise Http404

    def get(self, request, *args, **kwargs):
        print(kwargs.get("pk"))
        pk = kwargs.get("pk")
        publish = self.get_object(pk)
        serializer = PublishSerializer(publish)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        publish = self.get_object(pk)
        serializer = PublishSerializer(publish, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        publish = self.get_object(pk)
        publish.delete()
        return Response(status=200)


# 版本二 GenericAPIview 继承自APIView
#  在每个方法中都要区定义queryset和serializer，然后还需要验证字段信息，在post请求中的创建和更新
from rest_framework.generics import GenericAPIView


# 群查
class PublishGenericAPIview(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    # 重写GenericAPIView的get_queryset方法
    def get_queryset(self):
        queryset = super(PublishGenericAPIview, self).get_queryset()
        print(queryset)
        self.keyword = self.request.GET.get("keyword", '').strip()
        if self.keyword:
            queryset = queryset.filter(name__icontains=self.keyword)
        return queryset

    def get(self, request, *args, **kwargs):
        pub_queryset = self.get_queryset()
        pub_serializer = self.get_serializer(pub_queryset, many=True)
        return Response(pub_serializer.data)

    def post(self, request, *args, **kwargs):
        publish = self.get_serializer(data=request.data)
        if publish.is_valid():  # 验证来自于客户端的一个信息的增加，在验证之后会在serializer文件中去调用create方法将数据添加到数据库中
            publish.save()
            return Response(publish.data, status=200)
        return Response(publish.data, status=400)


class PublishDetailGenericAPIview(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    def get(self, request, *args, **kwargs):
        publish = self.get_object()
        serializer = self.get_serializer(publish)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        publish = self.get_object()
        serializer = self.get_serializer(publish, request.data)
        if serializer.is_valid():  # 来自客户端的一条数据的更新
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.data, status=400)

    def delete(self, request, *args, **kwargs):
        publish = self.get_object()
        publish.delete()
        return Response(status=200)


# 版本三  Mixins + GenericAPIView
from rest_framework import mixins
from rest_framework.generics import GenericAPIView


class PublishMixinGennerricAPIView(mixins.ListModelMixin,
                                   mixins.CreateModelMixin,
                                   GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer

    # 群查

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # 增加一个对象

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PublishDetailMixinGenericAPIView(mixins.RetrieveModelMixin,
                                       mixins.UpdateModelMixin,
                                       mixins.DestroyModelMixin,
                                       GenericAPIView):
    # 单查  带有pk属性的查询
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # 更新 带有pk属性的更新
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # 删除 带有pk属性的删除
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# 版本四
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


# 群查 和 创建


class PublishMixinAPIView(ListCreateAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


# 带有pk的查询 更新 删除


class PublishDetailMixinAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


# 版本五 viewset试图集， 重写as_as_view将增删改查（单查 多查）一起组合使用

from rest_framework import viewsets


class PublishViewSet(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


# 版本六 viewset + router    views文件中的就是最终的版本
from rest_framework import viewsets


class PublishViewSets(viewsets.ModelViewSet):
    queryset = Publish.objects.all()
    serializer_class = PublishSerializer


# Author views

from books.serializers2 import AuthorSerializer
from books.models import Author


class AutherViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Book views
from books.models import Book
from books.serializers2 import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
