from django.urls import path
from . import views

urlpatterns = [
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/', views.get_order_by_id, name='get_order_by_id'),

    path('orders/', views.get_all_orders, name='get_all_orders'),
    path('orders/status/<int:order_id>/', views.update_order_status, name='update_order_status'),
    path('orders/user/<int:user_id>/', views.get_user_specific_orders, name='get_user_specific_orders'),
    path('orders/stats/', views.get_order_stats, name='order_stats'),
]