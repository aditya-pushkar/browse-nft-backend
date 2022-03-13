from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination


from .models import Nft
from .serializers import NftSerializer

# Create your views here.
@api_view(['GET'])
def nfts(request):
    nft = Nft.objects.all()
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(nft, request)
    serializer = NftSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)

@api_view(['POST'])
def nft_uplode(request):
    user = request.user
    try:
        if user is not None:
            data = request.data
            title = data.get('title')
            img = data.get('img')
            eth_p = data.get('eth_price')
            redirect_link = data.get('redirect_link')
            tag1 = data.get('tag1')
            tag2 = data.get('tag2')
            tag3 = data.get('tag3')
            tag4 = data.get('tag4')

            nft = Nft.objects.create(
                user=user,
                title=title,
                img=img,
                eth_price=eth_p,
                redirect_link=redirect_link,
                tag1=tag1,
                tag2=tag2,
                tag3=tag3,
                tag4=tag4
            )
            serializer = NftSerializer(nft, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def nft_requested_user(request):
    try:
        user = request.user
        nft = Nft.objects.filter(username=user.username)
        serializer = NftSerializer(nft, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
def nft_delete(request, pk):
    try:
        user = request.user
        nft = Nft.objects.get(id=pk)
        if user == nft.user:
            nft.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['PUT'])
def nft_update(request, pk):
    try:
        user =  request.user
        nft = Nft.objects.get(id=pk)
        if user == nft.user:
            data = request.data
            nft.title = data.get('title')
            nft.img = data.get('img')
            nft.eth_p = data.get('eth_price')
            nft.redirect_link = data.get('redirect_link')
            nft.tag1 = data.get('tag1')
            nft.tag2 = data.get('tag2')
            nft.tag3 = data.get('tag3')
            nft.tag4 = data.get('tag4')

            nft.save()
            serializer = NftSerializer(nft, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print("ERROR --->", e)
        return Response({'details': f"{e}"},status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def nft_search(request):
    query = request.query_params.get('q')
    if query == None:
        query = " "
    nft = Nft.objects.filter(Q(title__icontains=query)|Q(tag1__icontains=query)|Q(tag2__icontains=query)|Q(tag3__icontains=query)|Q(tag4__icontains=query))
    paginator = PageNumberPagination()
    paginator.page_size = 10
    result_page = paginator.paginate_queryset(nft, request)
    serializer = NftSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)