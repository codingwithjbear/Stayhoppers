from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'listings'  # Replace 'your_app_name' with the actual name of your app

urlpatterns = [
    path('hello/', views.hello_world),
    path('grid/', views.all_listings)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
