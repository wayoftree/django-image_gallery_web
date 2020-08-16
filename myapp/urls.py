from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.main, name="main"),
	path('category/<int:cid>', views.cats_by_image, name="cats_by_image"),
	path('search/', views.search, name="search"),

]