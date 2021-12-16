from django.urls import path
from . import views

urlpatterns = [
    path('addlaptop/',views.addLaptop,name="add_laptop"),
    path('showlaptop/',views.showLaptop,name="show_laptop"),
    path('update/<int:i>/',views.updateView,name="update"),
    path('delete/<int:i>/',views.deleteView,name="delete"),
]