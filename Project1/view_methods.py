
from django.shortcuts import render
from django.http import request, HttpResponse
from Project1.users_list import *

# def home_method(request):
#     return HttpResponse("Django Project - Home");

def home_method(request):
    page_name = "Home"
    return render(request,
                  "home.html",
                  {"page_name_key": page_name})

def data_method(request, username):
    page_name = "Data"
    return render(request,
                  "data.html",
                  {"page_name_key" : page_name,
                   "username_key" : username})

def users_method(request):
    page_name = "Users"
    users = Users().users_list
    return render(request, "users.html",
                  {"page_name_key": page_name,
                   "users_list_key": users})

def specific_user_method(request, username):
    page_name = "Specific User"
    users = Users()
    users_list = users.users_list
    requested_users  = users.find_user(users_list, username)

    return render(request, "specific_user.html",
                  {"page_name_key": page_name,
                   "requested_user_key": requested_users,
                   "username_key": username})
