"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewsc
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('update_pass/', views.update_pass, name="update_pass"),
    path('update_profile/', views.update_profile, name="update_profile"),
    path('addMember/', views.addMember, name="addMember"),
    path('allMember/', views.allMember, name="allMember"),
    path('editMember/<int:pk>', views.editMember, name="editMember"),
    path('deleteMember/<int:pk>', views.deleteMember, name="deleteMember"),
    path('viewMember/<int:k>', views.viewMember, name="viewMember"),
    path('addNotice/', views.addNotice, name="addNotice"),
    path('allNotice/', views.allNotice, name="allNotice"),
    path('viewNotice/<int:k>', views.viewNotice, name="viewNotice"),
    path('forgotpassword/', views.forgotpassword, name="forgotpassword"),
    path('changepassword/', views.changepassword, name="changepassword"),
    path('firstTimeLogin/', views.firstTimeLogin, name="firstTimeLogin"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)