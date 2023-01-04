from . import views
from django.urls import path
urlpatterns = [
    path('home/',views.home, name='home'),
    path('save/',views.save , name='save'),
    path('save/sucessfull/',views.sucessfull , name='sucessfull'),
    path('change/',views.change , name='change'),
    path('delete/<int:pk>',views.delete_data , name='delete'),
    path('edit/<int:pk>',views.edit , name='edit')
]
