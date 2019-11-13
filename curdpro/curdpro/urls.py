from django.conf.urls import url
from django.contrib import admin
from curdapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index),
    url(r'^create/',views.create_view),
    url(r'^retrieve/',views.retrieve_view),
    url(r'^update/',views.update_view),
    url(r'^delete/',views.delete_view)
]