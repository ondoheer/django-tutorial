from django.conf.urls import url, patterns
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name="index"),
	url(r'^(?P<pk>[0-9]+)/$', views.SingleWineView.as_view(), name="single_wine"),
	url(r'^add_wine/', views.add_wine, name="add_wine"),
	url(r'^edit_wine/(?P<wine_id>[0-9]+)/$', views.edit_wine, name="edit_wine")
] 