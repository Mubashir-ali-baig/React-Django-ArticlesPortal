from ..api.views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'',ArticleViewSet, base_name='articles')
urlpatterns = router.urls


'''from django.urls import path

#from .views import ArticleDestroyView,ArticleUpdateView,ArticleListView,ArticleDetailView,ArticleCreateView

urlpatterns = [
    path('', ArticleListView.as_view()),
    path('<pk>', ArticleDetailView.as_view()),
    path('create/',ArticleCreateView.as_view()),
    path('<pk>/update/',ArticleUpdateView.as_view()),
    path('<pk>/delete/',ArticleDestroyView.as_view())
]
'''

