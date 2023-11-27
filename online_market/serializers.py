from rest_framework import serializers

from online_market.models import Good


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"

    @staticmethod
    def validate_price(value):
        if value <= 0:
            raise serializers.ValidationError("Price must be more than 0")
        return value

    @staticmethod
    def validate_amount(value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be more than 0")
        return value
