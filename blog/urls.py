from django.conf.urls import include, url
from . import views #Vistas: hacia donde se mapean. Consumen los modelos.
urlpatterns = [
    url(r'^$', views.post_list), #Lista de las urls
]
