from django.conf.urls import url
from parking import views


urlpatterns = [
    url(r'^$', views.index, name='parking_index'),
]


