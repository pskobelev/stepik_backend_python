from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from online_market.models import Good
from online_market.serializers import GoodsSerializer


class GoodApiTest(APITestCase):
    def test_get(self):
        good_1 = Good.objects.create(name="Сосиска", amount=4, price=69)
        good_2 = Good.objects.create(name="Жвачка", amount=2, price=10)
        url = reverse("goods-list")
        response = self.client.get(url)
        serializer_data = GoodsSerializer([good_1, good_2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
