"""CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from ser import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book/', views.BookView.as_view())
    # Serializer
    path('ser/book/', views.BookView.as_view()),
    re_path('ser/book/(?P<pk>\d+)', views.BookDetailView.as_view()),
    # path('ser/book/<int:pk>/', views.BookDetailView.as_view()),

    path('ser/publish/', views.PublishView.as_view()),
    re_path('ser/publish/(?P<pk>\d+)', views.PublishDetailView.as_view()),

    path('ser/author/', views.AuthorView.as_view({'get':'list', 'post':'create'})),
    re_path('ser/author/(?P<pk>\d+)', views.AuthorView.as_view({'get':'retrieve',
                                                                'put':'update',
                                                                'delete':'destroy'})),


]
