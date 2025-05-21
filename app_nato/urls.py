# from django.urls import path
# from .views import (
#     NatoMemberListAPIView,
#     NatoMemberCreateAPIView,
#     NatoMemberUpdateAPIView,
#     NatoMemberDetailAPIView,
#     NatoMemberDestroyAPIView
# )
# urlpatterns = [
#     path('members/create/', NatoMemberCreateAPIView.as_view(), name='member_create'),
#     path('members/update/<str:name>/', NatoMemberUpdateAPIView.as_view(), name='member_update'),
#     path('members/delete/<slug:slug>/', NatoMemberDestroyAPIView.as_view(), name='member_delete'),
#     path('members/<slug:slug>/', NatoMemberDetailAPIView.as_view(), name='member_detail'),
#     path('members/', NatoMemberListAPIView.as_view(), name='member_list'),
#
# ]

from rest_framework.routers import DefaultRouter

from app_nato.views import NatoMemberViewSet

router = DefaultRouter()
router.register('members', NatoMemberViewSet, basename='member')

urlpatterns = router.urls
