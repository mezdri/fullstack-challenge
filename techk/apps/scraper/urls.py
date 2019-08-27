from rest_framework import routers
from .viewsets import BookViewSet, ScraperView

router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register(r'scraper/', ScraperView.as_view())

urlpatterns = router.urls
