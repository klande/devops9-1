from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import Group, Permission

User = get_user_model()


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "phone", "email")


class UsersCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, style={'input_type': 'password'}, label='密码', write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password", "phone", "email")

    def create(self, validated_data):
        user = super(UsersCreateUpdateSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def get_groups(self, groups_queryset):
        ret = []
        for group in groups_queryset:
            ret.append({
                'id': group.id,
                'name': group.name
            })
        return ret

    def to_representation(self, instance):
        groups = self.get_groups(instance.groups.all())
        ret = super(UsersCreateUpdateSerializer, self).to_representation(instance)
        ret['users'] = {
            'id': instance.id,
            'username': instance.username,
            'email': instance.email,
            'phone': instance.phone
        }
        ret['groups'] = groups
        return ret


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')

    def member_info(self, member_queryset):
        ret = []
        for member in member_queryset:
            # 遍历queryset对象 并添加到ret中
            ret.append({
                'id': member.id,
                'username': member.username,
                'email': member.email,
                'phone': member.phone
            })
        return ret

    def permission_info(self, permission_queryset):
        ret = []
        for permission in permission_queryset:
            ret.append({
                'id': permission.id,
                'name': permission.name,
                'codename': permission.codename
            })
        return ret

    def to_representation(self, instance):
        # 展示给前端的数据
        # 将用户数据和权限数据返回前端，首先先要获取用户、权限对象
        members = self.member_info(instance.user_set.all())
        numbers = instance.user_set.count()
        permissions = self.permission_info(instance.permissions.all())
        ret = super(GroupsSerializer, self).to_representation(instance)
        ret['members'] = members
        ret['numbers'] = numbers
        ret['permissions'] = permissions
        return ret


class PermissionSerializer(serializers.ModelSerializer):
    """Permission序列化
        1： 返回Permission的基本信息
    """

    class Meta:
        model = Permission
        fields = ("id", "name", "codename")
