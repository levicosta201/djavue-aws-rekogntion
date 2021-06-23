from core import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/dapau$', views.dapau),
    url(r'^api/login$', views.login),
    url(r'^api/logout$', views.logout),
    url(r'^api/whoami$', views.whoami),

    url(r'^api/add_todo$', views.add_todo),
    url(r'^api/list_todos$', views.list_todos),

    url(r'^api/add_client$', views.add_client),
    url(r'^api/validate_client$', views.validate_client),
    url(r'^api/list_clients$', views.list_clients),
]
