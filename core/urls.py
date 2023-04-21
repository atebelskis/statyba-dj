from django.urls import path
from .views import main_page, user_login, UserRegisterView



# #User: Alfa
# #psw: Alfa1234

urlpatterns = [
        path('', main_page, name='index'),
        path('login/', user_login, name='login'),
        path('register', UserRegisterView.as_view(), name='register'),
        #path('logout')
]
