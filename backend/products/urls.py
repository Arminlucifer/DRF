from django.urls import path

from . import views


urlpatterns = [
    path('', views.ProductListCreateAPIview.as_view(), name="product-list"),
    path('<int:pk>/', views.ProductDetailAPIView.as_view(), name="product-detail"),
    path('<int:pk>/update/', views.ProductUpdateView.as_view(), name="product-update"),
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),


]
