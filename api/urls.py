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
    path('authors/<int:id>/', views.AuthorDetailByIdAPIView.as_view(), name='author-detail-id'),

]

