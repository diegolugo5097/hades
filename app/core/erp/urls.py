from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'
urlpatterns = [
    path('category/list/', Category_list_view.as_view(), name='category_list'),
    path('category/add/', Category_create_view.as_view(), name='category_create')
]
