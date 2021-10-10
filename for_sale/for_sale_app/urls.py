from .import views
from django.urls import path
app_name = 'for_sale_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:my_id>/', views.product_detail, name='product-detail'),
]
