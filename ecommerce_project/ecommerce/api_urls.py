from django.urls import path
from . import api_views

urlpatterns = [
    path("stores/", api_views.StoreListCreateView.as_view(), name="api-stores"),
    path("stores/<int:store_id>/products/", api_views.ProductListCreateView.as_view(), name="api-store-products"),
    path("products/<int:product_id>/reviews/", api_views.ReviewListView.as_view(), name="api-product-reviews"),
]