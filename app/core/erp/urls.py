from django.urls import path

from core.erp.views import my_first_view, my_second_view

urlpatterns =[
    path('uno/', my_first_view),
    path('dos/', my_second_view)
]