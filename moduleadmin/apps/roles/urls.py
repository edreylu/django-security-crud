from django.urls import path
from . import views


urlpatterns = [
    path('roles/', views.roles, name='roles'),
    path("roles/create/",views.createRole, name ="createRole"),
    path("roles/update/<int:id>",views.updateRole, name ="updateRole"),
    path("roles/update/",views.updateRole, name ="updateRole 2"),
    path("roles/delete/<int:id>",views.deleteRole, name ="deleteRole"),
]