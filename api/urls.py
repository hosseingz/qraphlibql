from django.urls import path 
from graphene_django.views import GraphQLView
from .schema import schema
from . import views

app_name = 'api'

urlpatterns = [
    # GRAPHQL API
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    
    
    
    # RESTFUL API
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    
    path('authors/', views.AuthorAPIView.as_view(), name='authors'),
    path('authors/<int:id>/', views.AuthorAPIView.as_view(), name='author-detail'),
    
    path('genres/', views.GenreAPIView.as_view(), name='genres-list'),
    path('genres/<int:id>/', views.GenreAPIView.as_view(), name='genre-detail'),


    path('books/create/', views.BookCreateAPIView.as_view(), name='book-create'),
    path('books/update/<int:id>/', views.BookUpdateAPIView.as_view(), name='book-update'),
    path('books/delete/<int:id>/', views.BookDestroyAPIView.as_view(), name='book-delete'),

    path('books/', views.BooksListAPIView.as_view(), name='books-list'),
    path('books/<int:id>/', views.BookDetailByIdAPIView.as_view(), name='book-detail'),

]

