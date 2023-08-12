from django.shortcuts import redirect

def is_authenticated(session):
    res = True if "username" not in session.keys() else False
    return res
