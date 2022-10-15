from django.urls import path
from .views import Food_View,Medicines_View,Other_amenities_View
urlpatterns = [
    path('food/',Food_View.as_view()),
    path('medicines/',Medicines_View.as_view()),
    path('other_amenities/',Other_amenities_View.as_view()),
]
