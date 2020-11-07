from django.urls import path
from usuario.views import RegistrarUser, UserList, UserUpdate



urlpatterns = [
    path('list-usuario/', UserList.as_view(), name='list_usuario'),
    path('new-usuario/', RegistrarUser.as_view(), name='new_usuario'),
    path('update-usuario/<int:pk>/', UserUpdate.as_view(), name='update_usuario'),

]
