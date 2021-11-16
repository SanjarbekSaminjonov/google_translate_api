from django.urls import path
from . import views


urlpatterns = [
    path('v1/get-only-text/<str:inp>/<str:out>/', views.get_only_text, name='get_only_text'),
]
