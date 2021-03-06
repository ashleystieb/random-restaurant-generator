"""eat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from restaurant import views as restaurant_views
from get_restaurant import views as result_views
from account.views import (login_view, create_person, logout_view, profile_view,
                           index_view, edit_profile, save_view, delete_view)
from eat import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restaurants/$', restaurant_views.list_view, name='list_view'),
    url(r'^restaurants/(?P<slug>[\w-]+)/', restaurant_views.item_view, name='item_view'),
    url(r'^search/$', result_views.return_restaurant, name='search'),
    url(r'^login$', login_view, name='user_login'),
    url(r'^register$', create_person, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', profile_view, name='profile'),
    url(r'^profile/(?P<username>[\w.@+-]+)/edit/$', edit_profile, name='edit_profile'),
    url(r'^search/saved/$', save_view, name='save'),
    url(r'^delete/(?P<pk>\d+)/$', delete_view, name='delete'),
    url(r'^$', index_view, name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
