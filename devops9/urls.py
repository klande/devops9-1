"""devops9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from users.router import users_router
from books.router import books_router
from rest_framework.routers import DefaultRouter
from books.view1 import PublishList, PublishDetail, PublishGenericAPIview, \
    PublishDetailGenericAPIview, PublishMixinGennerricAPIView, PublishDetailMixinAPIView, PublishMixinAPIView, \
    PublishViewSet

# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


router = DefaultRouter()
router.registry.extend(users_router.registry)
router.registry.extend(books_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include(router.urls)),

    # 请求生成jwt token.需要用户输入用户名密码
    # path('api/login/', obtain_jwt_token),
    # 刷新jwt_token,即让token失效，可以理解为登出
    # path('api/logout/', refresh_jwt_token),


    # 版本六
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # 版本一
    path('publish/', PublishList.as_view(), name="publishlist1"),
    re_path('publishdetail/(?P<pk>[0-9]+)?/', PublishDetail.as_view(), name="publishdetail"),

    #版本二
    path('publish2/', PublishGenericAPIview.as_view(), name="publish2"),
    re_path('publishdetail2/(?P<pk>[0-9]+)?/', PublishDetailGenericAPIview.as_view(), name="publishdetail2"),
    # 版本三：mixin+GenericAPI
    path('publishlist3/', PublishMixinGennerricAPIView.as_view(), name="publishlist3"),
    re_path('publishdetail3/(?P<pk>[0-9]+)?/', PublishMixinGennerricAPIView.as_view(), name='publish3_detail'),

    # 版本四：mixin各种排列组合+GenericAPI
    path('publishlist4/', PublishMixinAPIView.as_view(), name="publishlist4"),
    re_path('publishdetail4/(?P<pk>[0-9]+)?/', PublishDetailMixinAPIView.as_view(), name='publish4_detail'),

    # 版本五：viewset视图集，重写as_view将增删改查(单查+群查)函数绑定
    path('publishlist5/', PublishViewSet.as_view({"get": "list", "post": "create"}),
         name="publishlist5"),
    re_path('publishdetail5/(?P<pk>[0-9]+)?/',
            PublishViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}),
            name='publish5_detail'),

    path('api-auth/', include("rest_framework.urls")),

]



