"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from FirstApp import views # type: ignore
from MultiViewsApp import views as v
from app1 import views as q
from app2.views import q1
urlpatterns = [
    path('admin/', admin.site.urls),path('welcome/',views.display),
    path('welcome2/',views.show),path('dtime/',views.senddatetime),
    path('mrng/',v.f1),path('aftr/',v.f2),path('evng/',v.f3),path('time/',q.t1),
    path('img',q1),
]
