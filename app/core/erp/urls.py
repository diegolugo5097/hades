from django.urls import path
from core.erp.views.category.views import *

app_name = 'erp'
urlpatterns = [
    path('category/list/', category_list, name='category_list')
]
