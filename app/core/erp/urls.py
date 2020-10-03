from django.urls import path

from core.erp.views import my_first_view, my_second_view

app_name = 'erp'
urlpatterns = [
    path('uno/', my_first_view, name='vista1'),
    path('dos/', my_second_view, name='vista2')
]
