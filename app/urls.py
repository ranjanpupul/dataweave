from django.conf.urls import include, url
from app.views import ProductDataApi, DiscountBucketApi
from rest_framework import routers
router = routers.SimpleRouter()


urlpatterns = [
    url(r'^productInfo/', ProductDataApi.as_view()),
    url(r'^productInfoget/', ProductDataApi.as_view()),
    url(r'^discountBucket/', DiscountBucketApi.as_view()),
    url(r'^', include(router.urls)),
]