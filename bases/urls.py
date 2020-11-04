from django.urls import path
from django.contrib.auth import views as auth_views
from bases.views import Home, Login


urlpatterns = [
    path('', Login.as_view(), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='homepage/index.html'),name='logout'),
    path('home/',Home.as_view(), name='home'),
]
