#from django.contrib import admin
#from django.urls import path, include
#from datas import views

#urlpatterns = [
 #   path('admin/', admin.site.urls),
 #   path('datas/', include('datas.urls')),

  #  path('login/', views.user_login, name="user_login"),
  #  path('', views.home, name="home"),
  #  path('logout/', views.user_logout, name="user_logout"),
#]

from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import home
from managerusers.views import AddManagerUser, DelManagerUser, ActiveManagerRole, DeactiveManagerRole
from tables.views import water, hotwater, temperature, warm, electricity

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),  
    path('', home, name='home'),
    path('hotwater/', hotwater, name='hotwater'),
    path('water/', water, name='water'),
    path('warm/', warm, name='warm'),
    path('temperature/', temperature, name='temperature'),
    path('electricity/', electricity, name='electricity'),
    path('profile/', AddManagerUser, name='profile'),
    path('profile/deletemaneger/', DelManagerUser, name='delmanager'),
    path('profile/activerole/', ActiveManagerRole, name='activerole',),
    path('profile/deactiverole/', DeactiveManagerRole, name='deactiverole'),
]