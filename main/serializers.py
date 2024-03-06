from rest_framework import serializers
from .models import *


class BannerSerializres(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"


class RecomendationSerializres(serializers.ModelSerializer):
    class Meta:
        model = Recomendation
        fields = "__all__"


class SellSerializres(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = "__all__"


class DetailSerializres(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = "__all__"


class PresintaitonSerializres(serializers.ModelSerializer):
    class Meta:
        model = Presintaiton
        fields = "__all__"


class TestimonialSerializres(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"


class About_usSerializres(serializers.ModelSerializer):
    class Meta:
        model = About_us
        fields = "__all__"


