from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users, name='users'),
    path('users/<int:id>', views.usersById, name='usersById'),
    path("users/create/",views.create, name ="create"),
    path("users/update/<int:id>",views.update, name ="update"),
]