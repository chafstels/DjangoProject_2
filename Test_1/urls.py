from .views import PostAPIView, CommentAPIView
from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'post', PostAPIView, basename='post')
router.register(r'comment', CommentAPIView, basename='comment')


urlpatterns = [
    # path('post/', PostAPIView.as_view({'get': 'list'})),
    # path('comment/', CommentAPIView.as_view({'get': 'list'})),
    path('', include(router.urls)),
]