from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('article', views.ModelArticleViewSet, basename='article')
app_name = 'api_basic'
urlpatterns = [
    path('viewset/', include(router.urls)),
    path('articles/', views.ArticleAPIView.as_view(), name='articles'),
    path('articles/<int:id>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('generic/articles/', views.GenericAPIView.as_view()),
    path('generic/articles/<int:id>/', views.GenericAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    # path('articles-2/', views.ArticleAPIView.as_view(), ),
    # path('article-details-2/<int:id>/', views.ArticleDetailView.as_view()),
]