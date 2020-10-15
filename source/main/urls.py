"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from source.api_v1.views import json_echo_view, get_token_view, add_view, subtract_view, multiply_view, divide_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('echo',json_echo_view),
    path('get_token', get_token_view),
    path('add/', add_view),
    path('subtract/', subtract_view),
    path('multiply/', multiply_view),
    path('divide/', divide_view)

]
