from django.urls import path
from . import views


urlpatterns = [
    path('formas/', views.formasMenu, name='formasMenu'),
    path("formas/create/",views.createFormas, name ="createFormas"),
    path("formas/update/<int:id>",views.updateFormas, name ="updateFormas"),
    path("formas/update/",views.updateFormas, name ="updateFormas 2"),
    path("formas/delete/<int:id>",views.deleteFormas, name ="deleteFormas"),
]