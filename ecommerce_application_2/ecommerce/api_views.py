from rest_framework import generics, permissions
from .models import Store, Product, Review
from .serializers import StoreSerializer, ProductSerializer, ReviewSerializer


class StoreListCreateView(generics.ListCreateAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(vendor=self.request.user)


class ProductListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        store_id = self.kwargs["store_id"]
        return Product.objects.filter(store_id=store_id)

    def perform_create(self, serializer):
        store_id = self.kwargs["store_id"]
        serializer.save(store_id=store_id)


class ReviewListView(generics.ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        return Review.objects.filter(product_id=product_id)
