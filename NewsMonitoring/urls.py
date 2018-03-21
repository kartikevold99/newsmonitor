"""NewsMonitoring URL Configuration

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


from login.forms import CustomAuthForm
from django.contrib.auth.views import login
from django.urls import path
from login import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', login, name='login', kwargs={"authentication_form": CustomAuthForm}),
    path('logout/', views.logout_page),
    path('accounts/login/', login),
    path('sign_up/', views.register),
    path('register_success/', views.register_success),
    path('home/', views.home),
    path('add_source/', views.add_source),
    path('sources_list/', views.sources_list),
    path('remove_source/', views.remove_source),
    path('search_source/', views.search_source),
    path('edit_source/', views.edit_source),
    path('fetch_story/', views.fetch_story),
    path('stories_list/', views.stories_list),
    path('search_stories/', views.search_stories),
    path('remove_story/', views.remove_story),
    path('add_story/', views.add_story),
    path('edit_story/', views.edit_story)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
