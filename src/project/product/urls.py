from django.urls import path, include

from rest_framework import routers

from .views import CategoryView

from . import views

app_name = "product"

router = routers.SimpleRouter()
router.register("category", views.CategoryView)
router.register("brand", views.BrandView)
router.register("product", views.ProductView)


urlpatterns = [
    path("", include(router.urls))
]
