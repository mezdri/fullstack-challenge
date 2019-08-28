from rest_framework import routers
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .viewsets import BookViewSet, ScraperView
from django.views.decorators.csrf import csrf_exempt

# router = routers.SimpleRouter()
# router.register('books', BookViewSet)
# router.register('scraper/', ScraperView)

# urlpatterns = router.urls

urlpatterns = [
    path('books/', csrf_exempt(BookViewSet.as_view({'get': 'list'}))),
    path('scraper/', csrf_exempt(ScraperView.as_view({'post': 'post'}))),
]

urlpatterns = format_suffix_patterns(urlpatterns)
