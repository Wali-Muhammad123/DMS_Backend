from django.urls import path
from .views import FamilyView,OccupentView,CampView
urlpatterns = [
    path('family/',FamilyView.as_view()),
    path('occupent/',OccupentView.as_view()),
    path('camps/',CampView.as_view())
]
