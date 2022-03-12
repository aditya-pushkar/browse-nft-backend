from django.urls import path

from .views import nfts, nft_uplode, nft_requested_user, nft_delete, nft_update,nft_search


app_name = 'nft'

urlpatterns = [
    path('all/', nfts, name='nfts'),
    path('uplode/', nft_uplode, name='nft_uplode'),
    path('my-nft/', nft_requested_user, name='nft_my'),
    path('delete/<str:pk>/', nft_delete, name='nft_delete'),
    path('update/<str:pk>/', nft_update, name='nft_update'),
    path('search/', nft_search, name='search'),
]
