from django.urls import path
from TourSite.views import main_page

urlpatterns = [
    path("", main_page)
]