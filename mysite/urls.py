"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import main.views as main_view
import guestbook.views as guestbook_view
import user.views as userviews
import board.views as boardviews

urlpatterns = [
    path('admin/', admin.site.urls),

    path('main/', main_view.index),
    path('guestbook/', guestbook_view.index),
    path('guestbook/insert', guestbook_view.insert),
    path('guestbook/deleteform', guestbook_view.deleteform),
    path('guestbook/delete', guestbook_view.delete),

    path('user/joinform', userviews.joinform),
    path('user/join', userviews.join),
    path('user/joinsuccess', userviews.joinsuccess),
    path('user/loginform', userviews.loginform),
    path('user/login', userviews.login),
    path('user/logout', userviews.logout),
    path('user/updateform', userviews.updateform),
    path('user/update', userviews.update),

    path('board/', boardviews.index),
    path('board/view', boardviews.view),
    path('board/modifyform', boardviews.modifyform),
    path('board/modify', boardviews.modify),
    path('board/write', boardviews.write),
]
