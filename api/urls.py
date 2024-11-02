from django.urls import path 
from graphene_django.views import GraphQLView
from . import views

app_name = 'api'

urlpatterns = [
    # GRAPHQL API
    path("graphql", GraphQLView.as_view(graphiql=True)),
    
    
    
    # RESTFUL API
    path('signup/', views.SignupAPIView.as_view(), name='signup'),
    path('login/', views.UserLoginAPIView.as_view(), name='login'),
    
    
    path('authors/create/', views.AuthorCreateAPIView.as_view(), name='author-create'),
    path('authors/update/<int:id>/', views.AuthorUpdateAPIView.as_view(), name='author-update'),
    path('authors/delete/<int:id>/', views.AuthorDestroyAPIView.as_view(), name='author-delete'),

    path('authors/', views.AuthorsListAPIView.as_view(), name='authors-list'),
    path('authors/<int:id>/', views.AuthorDetailByIdAPIView.as_view(), name='author-detail'),
    
    
    path('genres/create/', views.GenreCreateAPIView.as_view(), name='genre-create'),
    path('genres/update/<int:id>/', views.GenreUpdateAPIView.as_view(), name='genre-update'),
    path('genres/delete/<int:id>/', views.GenreDestroyAPIView.as_view(), name='genre-delete'),

    path('genres/', views.GenresListAPIView.as_view(), name='genres-list'),
    path('genres/<int:id>/', views.GenreDetailByIdAPIView.as_view(), name='genre-detail'),


    path('books/create/', views.BookCreateAPIView.as_view(), name='book-create'),
    path('books/update/<int:id>/', views.BookUpdateAPIView.as_view(), name='book-update'),
    path('books/delete/<int:id>/', views.BookDestroyAPIView.as_view(), name='book-delete'),

    path('books/', views.BooksListAPIView.as_view(), name='books-list'),
    path('books/<int:id>/', views.BookDetailByIdAPIView.as_view(), name='book-detail'),

]

