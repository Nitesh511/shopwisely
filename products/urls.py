from django.urls import path
from .import views
urlpatterns = [
    path('homepage' ,views.homepage),
    path('category_form',views.category_form),
    path('get_category',views.get_category),
    path('delete_category/<int:category_id>', views.delete_category),
    path('update_category/<int:category_id>', views.category_update_form),


    path('product_form',views.product_form),
    path('get_product',views.get_product),
    path('delete_product/<int:product_id>', views.delete_product),
    path('update_product/<int:product_id>', views.product_update_form),

    path('get_category_user',views.show_categories),
    path('get_product_user', views.show_products),
    path('add_to_cart/<int:product_id>', views.add_to_cart),
    path('mycart',views.show_cart_items),
    path('remove_cart_item/<int:cart_id>', views.remove_cart_item),
    path('order_form/<int:product_id>/<int:cart_id>',views.order_form),
    path('my_order', views.my_order),
    path('menu/<int:cat_id>', views.category_button),



]