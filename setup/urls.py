"""setup URL Configuration

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
from django.urls import path, include
from . import views


## Controller/URL to register all the APP created in within the project.
urlpatterns = [
    path('user/', include('user.urls')),
    path('', views.index, name='_index'),
    path('home', views.home, name='_home'),
    path('handle_form', views.handle_form, name='handle_form'),
    path('delete_user/<id>', views.delete_user, name='delete_user'),
    path('edit_user/<id>', views.edit_user, name='edit_user'),
    path('update_record', views.update_record, name='update_record'),
    path('logout', views.logout, name="logout"),
    path('deleteSelected', views.deleteSelected, name='deleteSelected'),
]
