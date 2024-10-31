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
    
]
