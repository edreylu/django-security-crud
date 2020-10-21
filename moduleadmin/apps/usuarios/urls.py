from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.users, name='users'),
    path('users/<int:id>', views.usersById, name='usersById'),
    path("users/create/",views.createUser, name ="createUser"),
    path("users/update/<int:id>",views.updateUser, name ="updateUser"),
    path("users/update/",views.updateUser, name ="updateUser 2"),
    path("users/delete/<int:id>",views.deleteUser, name ="deleteUser"),
]