from rest_framework.serializers import ModelSerializer

from .models import Nft

# class TagSerializer(ModelSerializer):

#     class Meta:
#         model = Tag
#         fields = ['name']


class NftSerializer(ModelSerializer):
    # tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Nft
        exclude = ['user']