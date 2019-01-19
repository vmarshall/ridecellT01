"""ridecellT01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from parking import views as parking_views
from rest_framework_swagger.views import get_swagger_view
from rest_framework.schemas import get_schema_view

simple_router = DefaultRouter()

simple_router.register(r'parking', parking_views.ParkingSpotViewSet)
simple_router.register(r'users', parking_views.UserViewSet)

# simple_router.register(r'search', parking_views.SearchByRadiusList)
# simple_router.register(r'groups', parking_views.GroupViewSet)

swagger_view = get_swagger_view(title='Ridecell API (swagger)')
schema_view = get_schema_view(title='Ridecell API (core)')

urlpatterns = [
    path('v1/api/', include(simple_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    url(r'^docs/', include_docs_urls(title='Ridecell Parking API')),
    url(r'^schema/$', schema_view),
    url(r'^', include('parking.urls'))

]
