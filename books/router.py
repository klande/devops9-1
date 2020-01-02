from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, PublishViewSet
# from .view1 import PublishViewSet, AutherViewSets, BookViewSet,

books_router = DefaultRouter()
books_router.register(r'books', BookViewSet, base_name="books")
books_router.register(r'author', AuthorViewSet, base_name="author")
books_router.register(r'publish', PublishViewSet, base_name="publish")
