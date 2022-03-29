from django.urls import path

from .views import nft_unapproved, nft_reject, nft_approve

app_name = 'staff_panel'

urlpatterns = [
    path('unapproved/', nft_unapproved, name='unapproved'),
    path('reject/<str:pk>/', nft_reject, name='reject'),
    path('approve/<str:pk>/', nft_approve, name='approve'),
]
