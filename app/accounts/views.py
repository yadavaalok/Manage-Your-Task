from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import View


class Register(View):

    def get(self, request):
        return render(request, "register.html")
    

class Login(View):

    def get(self, request):
        return render(request, "login.html")
    

class ResetPassword(View):

    def get(self, request):
        return render(request, "reset_password.html")