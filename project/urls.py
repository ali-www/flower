
from django.contrib import admin
from django.urls import path , include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    #============= the urls for translate 
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(

    path('admin/', admin.site.urls),
    path('',include('flower.urls')),
    path('',include('like.urls')),
    path('account/',include('register.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

) 