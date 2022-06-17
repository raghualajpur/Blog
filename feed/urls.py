from django.urls import path
from .views import HomePageView, postDetailVeiw
app_name='feed'


urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('detail/<int:pk>/',postDetailVeiw.as_view(), name='detail'),
]
