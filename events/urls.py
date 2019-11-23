from django.urls import path
from .views import *

urlpatterns = [
    path('', homePage),
    path('about', aboutPage),
    path('contact', contactPage),
    path('<slug:catagory>', catagoryListing),
    path('<slug:catagory>/<slug:event_slug>', eventListing),
]