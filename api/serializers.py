from django.conf.urls import url, include
from archive.models import *
from rest_framework import routers, serializers, viewsets
from .utils import  ChoicesSerializerField

# Serializers define the API representation.
class NewAnnoncementSerializer(serializers.ModelSerializer):
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