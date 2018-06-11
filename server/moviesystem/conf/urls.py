"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

# from controlers.usercontroler import UserControler

# user_controler = UserControler()

urlpatterns = [
    # url(r'^api/auth/token_id$', user_controler.getTokenControler),
    # url(r'^api/auth/verify$', user_controler.tokenVerifyControler),
    # url(r'^api/users/register$', user_controler.registerControler),
    # url(r'^api/users/login$', user_controler.loginControler),
    # url(r'^api/users/(?P<user_id>[0-9A-Za-z]+$)$', user_controler.getUserByIdControler),
]
