from django.contrib import admin
from django.urls import path, include
from datas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('datas/', include('datas.urls')),

    path('login/', views.user_login, name="user_login"),
    path('', views.home, name="home"),
    path('logout/', views.user_logout, name="user_logout"),
]
