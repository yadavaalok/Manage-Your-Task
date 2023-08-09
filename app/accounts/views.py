from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views import View


class Register(View):

    def get(self, request):
        return render(request, "register.html")
    
    def post(self, request):
        user_data = request.POST
        first_name = user_data.get('first_name')
        last_name = user_data.get('last_name')
        username = user_data.get('username')
        email = user_data.get('email')
        password = user_data.get('password')
        confirm_password = user_data.get('confirm_password')

        if password!=confirm_password:
            return render(request, "register.html")
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        return redirect('login')
    

class Login(View):

    def get(self, request):
        return render(request, "login.html")
    
    def post(self, request):
        user_data = request.POST
        username = user_data.get('username')
        password = user_data.get('password')
        print()
        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('homepage')
        else:
            return render(request, "login.html")
    

class ResetPassword(View):

    def get(self, request):
        return render(request, "reset_password.html")
    
    def post(self, request):
        user_data = request.POST
        user = User.objects.get(username=user_data.get('username'))
        if user is not None:
            if user.email == user_data.get('email'):
                if user_data.get('password') == user_data.get('confirm_password'):
                    user.set_password(user_data.get('password'))
                    user.save()
                    return redirect('login')
        return render(request, 'reset_password.html')
