from django.urls import path, include
from homepage.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]