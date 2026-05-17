from rest_framework import serializers
from rest_framework.reverse import reverse

from api.serializers import UserPublicSerializer

from . validators import validate_title
from . models import Product


class ProductSerializer(
        serializers.ModelSerializer):

    user = UserPublicSerializer(source='owner', read_only=True)

    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)
    title = serializers.CharField(validators=[validate_title])

    class Meta:
        model = Product
        fields = [
            'id',
            'url',
            'edit_url',
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
            'user',

        ]

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-update", kwargs={"pk": obj.pk}, request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return obj.get_discount()


class ProductDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price"
        ]
