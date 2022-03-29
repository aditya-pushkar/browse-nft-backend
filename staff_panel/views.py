"""       nft approval and rejection panel for staff      """

from functools import partial
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

from nft.models import Nft
from nft.serializers import NftSerializer


# Views 

@api_view(['GET'])
def nft_unapproved(request):
    try:
        nft = Nft.objects.filter(approved=False)
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(nft, request)
        serializer = NftSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    except Exception as e:
        return Response({'error': f'{e}'})


@api_view(['PATCH'])
def nft_approve(request, pk):
    try:
        nft = Nft.objects.get(id=pk)
        serializer = NftSerializer(nft, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        return Response({'error': f'{e}'}, status=status.HTTP_204_NO_CONTENT)



@api_view(['DELETE'])
def nft_reject(request, pk):
    try:
        nft = Nft.objects.get(id=pk)
        if request.user.is_staff == True:
            nft.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)  
    except Exception as e:
        return Response({'error': f'{e}'})