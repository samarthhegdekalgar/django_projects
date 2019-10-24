from django.urls import path, include
from .views import CategoryList, index

urlpatterns = [
    path('', index, name='index'),
    # path('category/', api_category_view, name='categories-list'),
    # path('category/<pk>/', api_category_view, name='single-data'),
    # path('guest/', api_guests_list_view, name='guest-list')
    path('category/', CategoryList.as_view(), name='category-list')
]