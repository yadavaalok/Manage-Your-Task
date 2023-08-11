from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views import View
import re


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

        # Check passwords are same
        if password!=confirm_password:
            msg = "Password Does Not Match !!!"
            return render(request, "register.html", {'msg': msg})
        # Check the username is unique
        if User.objects.filter(username=username).exists():
            msg = "Username Already Exists!!"
            return render(request, 'register.html', {'msg': msg})
        #Check the email is unique
        if User.objects.filter(email=email).exists():
            msg = "Email Id already registered"
            return render(request, 'register.html', {'msg': msg})
        # Validate password
        if not self.is_valid_password(password):
            msg = "Password is weak. Please use combination of Uppercase, Symbols and numbers."
            return render(request, 'register.html', {'msg': msg})
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
        user.save()
        return redirect('login')   

    def is_valid_password(password):
        pattern = r'^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{8,}$'
        return re.match(pattern, password) is not None    


class Login(View):

    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        user_data = request.POST
        username = user_data.get('username')
        password = user_data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            request.session['username'] = username
            return redirect('homepage')
        else:
            msg = "Invalid Credentials!!"
            return render(request, "login.html", {'msg': msg})


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
                else:
                    msg = "Password does not match!!!"
                    return render(request, 'reset_password.html', {'msg': msg})
            else:
                msg = "Invalid User details!!!"
                return render(request, 'reset_password.html', {'msg': msg})
        else:
            msg = "User does not exists!!!"
            return render(request, 'reset_password.html', {'msg': msg})



class Logout(View):

    def get(self, request):
        request.session.clear()
        return redirect('login')
