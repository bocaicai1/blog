"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('myblog_yangbo/', include(('myblog_yangbo.urls','myblog_yangbo'),namespace='myblog_yangbo')),

=======

    path('blog_hxq/', include('blog_hxq.urls', namespace='blog')),
    path('blog_zhaojianbing/',include('blog_zhaojianbing.urls',namespace = 'blog_zhaojianbing')),
    path('blog/', include('blog.urls', namespace='blog')),
    path('MoTangS/',include('motangsTest.urls')),
>>>>>>> 4ffb17588015301ddb9ade58b4addfc6cdecfa2a
]
