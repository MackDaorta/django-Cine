from django.contrib import admin
from django.shortcuts import render, redirect
def panel_admin(request):
    if not request.user.is_auhenticated or not request.user.is_staff:
        return redirect('home')
# Register your models here.
