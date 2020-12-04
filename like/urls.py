
from django.urls import path
from  .views import LikeFlowerView
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
 
    path('flower/<int:flower_id>/action/',LikeFlowerView.as_view(),name='like-flower'),
   


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)