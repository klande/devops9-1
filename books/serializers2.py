from rest_framework import serializers
from .models import Publish, Author, Book


#
#
# # 版本一


class PublishSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30, required=True, help_text="出版商名")
    city = serializers.CharField(max_length=60, required=True, help_text="出版商城市")
    address = serializers.CharField(max_length=60, required=True, help_text="出版商地址")

    def create(self, validated_data):
        print(validated_data)
        print("3333")
        return Publish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.city = validated_data["city"]
        instance.address = validated_data["address"]
        instance.save()
        return instance


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, required=True, help_text="作者名字")
    email = serializers.EmailField(max_length=50, help_text="作者邮箱")
    phone = serializers.CharField(max_length=20, help_text="联系电话")
    address = serializers.CharField(max_length=60, help_text="作者地址")

    def create(self, validated_data):
        print(validated_data)
        return Author.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.email = validated_data["email"]
        instance.phone = validated_data["phone"]
        instance.address = validated_data["address"]
        instance.sava()
        return instance


#
#
# from .models import Book
#
#
# 第二版本
# class BookSerializer(serializers.Serializer):
#     # name = serializers.CharField(max_length=50, required=True, help_text="书本名称")
#     # authors = serializers.CharField(max_length=50, required=True, help_text="作者名字")
#     # publisher = serializers.CharField(required=True, help_text="出版社名称")
#     # publication_date = serializers.DateField(required=True, help_text="出版日期")
#     publisher = PublishSerializer(many=False)
#     authors = AuthorSerializer(many=True)
#     publication_date = serializers.DateField(format="%Y-%m-%d")
#
#     name = serializers.CharField(max_length=100, required=True, help_text="书本名称")
#     authors = authors
#     publisher = publisher
#     publication_date = publication_date
#
#     def create(self, validated_data):
#         print(validated_data)
#         print("2222")
#
#         author_list = validated_data.pop("authors", [])
#         publisher = validated_data.pop("publisher", "")
#         print(publisher)
#         print(dict(publisher))
#         p = Publish.objects.get(name=dict(publisher)['name'])
#         print(p)
#         validated_data['publisher'] = p
#         instance = Book.objects.create(**validated_data)
#         authors = []
#         for author in author_list:
#             author = Author.objects.get(name=dict(author)['name'])
#             authors.append(author)
#         instance.authors.add(*authors)
#         return instance

# 第三版本
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def author(self, author_queryset):
        ret = []
        for author in author_queryset:
            ret.append({
                'id': author.id,
                'name': author.name,
                'email': author.email
            })
        return ret

    def to_representation(self, instance):
        # 返回给前端的数据
        publisher_obj = instance.publisher
        authors_obj = self.author(instance.authors.all())
        ret = super(BookSerializer, self).to_representation(instance)

        ret['publisher'] = {
            'id': publisher_obj.id,
            'name': publisher_obj.name,
            'address': publisher_obj.address
        }
        ret['authors'] = authors_obj
        return ret
