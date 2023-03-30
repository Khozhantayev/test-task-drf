from django.contrib import admin
from django.urls import path, include, re_path
from apiproject.views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/postslist/', PostAPIList.as_view()),
    path('api/v1/postslist/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/v1/postsdelete/<int:pk>/', PostAPIDetailView.as_view()),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/postslist/', PostViewSet.as_view({'get': 'list'})),
    # path('api/v1/postslist/<int:pk>/', PostViewSet.as_view({'put': 'update'})),
]



# class CustomRouter(routers.SimpleRouter):
#     routers = [
#         routers.Route(url=r'^{prefix}$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'List'}),
#         routers.Route(url=r'^{prefix}/{lookup}$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]


# router = CustomRouter()
# router.register(r'posts', PostViewSet, basename='posts')