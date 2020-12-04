
from django.urls import path
from  .views import FlowerDetailView, HomeView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView ,LogoutView



urlpatterns = [
    path('',HomeView.as_view()),
    path('flower/<int:pk>/',FlowerDetailView.as_view(),name='flower-detal'),
    #================================================================================== start loing and logout ===
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
      #================================================================================== end  loing and logout ===


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
