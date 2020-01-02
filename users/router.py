from rest_framework.routers import DefaultRouter
from .views import UsersViewset, GroupsViewset, PermissionsViewset, UsersCreateUpdateViewset

users_router = DefaultRouter()
users_router.register(r'user', UsersViewset, base_name="user")
users_router.register(r'group', GroupsViewset, base_name="group")
users_router.register(r'per', PermissionsViewset, base_name="per")
users_router.register(r'user_create_update', UsersCreateUpdateViewset, base_name="user_create_update")
