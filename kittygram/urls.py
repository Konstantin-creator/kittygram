from django.urls import include, path

# from cats.views import cat_list
from cats.views import CatList, CatDetail, CatViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('cats', CatViewSet)

urlpatterns = [
   path('', include(router.urls)),
   # path('cats/', CatList.as_view()),
   # path('cats/<int:pk>/', CatDetail.as_view()),
]
