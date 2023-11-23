from rest_framework import serializers

from online_market.models import Good


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be more than 0")
        return value

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be more than 0")
        return value
