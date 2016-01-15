from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name="new_list"),
    url(r'^(\d+)/$', views.view_list, name = 'view_list'),
    url(r'^(\d+)/items/$', views.edit_list, name = "edit_list"),
    url(r'^(\d+)/item/(\d+)/delete$', views.delete_item, name = 'delete_item'),
]
