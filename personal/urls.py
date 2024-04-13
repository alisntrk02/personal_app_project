from django.urls import path, include

from .views import DepartmanListCreateAPIView, PersonalListCreateAPIView, DepartmanDetail, PersonalDetail

urlpatterns = [
    path('departman/', DepartmanListCreateAPIView.as_view()),
    path('departman/<int:pk>/', DepartmanDetail.as_view()),
    path('', PersonalListCreateAPIView.as_view()),
    path('<int:pk>/', PersonalDetail.as_view()),
]