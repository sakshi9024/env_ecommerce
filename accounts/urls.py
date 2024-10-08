from django.urls import path
from accounts.views import loginpage, registerpage

urlpatterns = [
    path('login/', loginpage , name="login"),
    path('register/', registerpage, name="register")
]