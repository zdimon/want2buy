from django.conf.urls import url, include
from archive.models import *
from rest_framework import routers, serializers, viewsets
from .utils import  ChoicesSerializerField
from account.models import Profile
from django.contrib.auth.models import User

# Serializers define the API representation.
class NewAnnoncementSerializer(serializers.ModelSerializer):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20

    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    sub_sub_category = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    once = ChoicesSerializerField() 
    type = ChoicesSerializerField()
    opt_roznica = ChoicesSerializerField()
    new_bu = ChoicesSerializerField()
    class Meta:
        model = NewAnnouncement
        fields = (
                'id',
                'title', 
                'user', 
                'category', 
                'sub_category',
                'sub_sub_category',
                'new_category',
                'new_bu',
                'opt_roznica',
                'type',
                'once',
                'price',
                'region',
                'city',
                'created_at',
                'thumbnail'
                )
        #fields = '__all__'


from django.conf.urls import url, include
from archive.models import *
from rest_framework import routers, serializers, viewsets
from .utils import  ChoicesSerializerField

# Serializers define the API representation.
class AnnoncementSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    sub_category = serializers.StringRelatedField()
    sub_sub_category = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    created_at = serializers.StringRelatedField()
    once = ChoicesSerializerField() 
    type = ChoicesSerializerField()
    opt_roznica = ChoicesSerializerField()
    new_bu = ChoicesSerializerField()
    class Meta:
        model = Announcement
        fields = (
                'id',
                'title', 
                'user', 
                'category', 
                'sub_category',
                'sub_sub_category',
                'new_category',
                'new_bu',
                'opt_roznica',
                'type',
                'once',
                'price',
                'region',
                'city',
                'created_at',
                'thumbnail'
                )
        #fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = (
                'user_id',
                'first_name', 
                'last_name', 
                'full_name'
                )


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = (
                'id',
                'username', 
                'email', 
                'profile'
                )


class OfferSerializer(serializers.ModelSerializer):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 20
    seller = UserSerializer()
    buyer = UserSerializer()
    announcement = serializers.StringRelatedField()
    created_at = serializers.DateTimeField(format='iso-8601')

    class Meta:
        model = Offer
        fields = (
                'id',
                'seller',
                'buyer',
                'is_current',
                'buyer_id',
                'message',
                'price',
                'created_at',
                'announcement',
                'url',
                'image',
                'file',
                'status',
                'announcement',
                'announcement_id'
                )