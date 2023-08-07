"""
URL configuration for PROJECT_42__cbv__using__Template_View__creating_Model_form__ project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

## rendering from Url Mapping Directly so we import this
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_rendering/',data_rendering.as_view(),name='data_rendering'),
    path('fbv_insert/',fbv_insert,name='fbv_insert'),
    path('Cbv_insert/',Cbv_insert.as_view(),name='Cbv_insert'),
    
    ## rendering from Url Mapping Directly by using this 
    path('tushar/',TemplateView.as_view(template_name='index.html'),name='tushar')
]
