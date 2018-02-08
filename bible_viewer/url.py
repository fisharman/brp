from django.urls import path, register_converter
from . import views, converters

register_converter(converters.DateConverter, 'date')

urlpatterns = [
    # direct visits to the site bring up default
    path('', views.index, name='index'),
    path('<str:version>/', views.index, name='version'),
    path('<str:version>/<date:date>/', views.set_date, name ='set_date')


    # Todo 1: disable JS datepicker for mobile
    # Todo 6: 404 should fail gracefully
    # Todo 7: use cookies to remember last selected version

]

