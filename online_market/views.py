from uuid import uuid4

from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
    HTTP_201_CREATED,
)
from rest_framework.views import APIView

from online_market.models import Good, Token
from online_market.serializers import GoodsSerializer


def get_token(request):
    rand_token = Token()
    rand_token.token_id = uuid4()
    rand_token.save()
    return JsonResponse({"token": rand_token.token_id})


class GoodsAPI(APIView):
    class Meta:
        model = Good
        fields = ["name", "amount", "price"]

    def get(self, request):
        tokens_id = list(token.token_id for token in Token.objects.all())
        try:
            if request.GET["token"] in tokens_id:
                serializer = GoodsSerializer(Good.objects.all(), many=True)
                return Response(serializer.data, status=HTTP_200_OK)
            else:
                return HttpResponse(
                    "Token is invalid", status=HTTP_401_UNAUTHORIZED
                )
        except KeyError:
            return HttpResponse(
                "Token must be present", status=HTTP_401_UNAUTHORIZED
            )

    def post(self, request):
        tokens_id = list(token.token_id for token in Token.objects.all())

        if not request.GET.get("token", False):
            return HttpResponse(
                "Token must be present", status=HTTP_401_UNAUTHORIZED
            )
        elif request.GET.get("token", False) in tokens_id:
            new_good = GoodsSerializer(data=request.data)
            if new_good.is_valid():
                new_good.save()
                return HttpResponse(
                    "New good has been added", status=HTTP_201_CREATED
                )
            else:
                return JsonResponse(new_good.errors)
        else:
            return HttpResponse(
                "Token is invalid", status=HTTP_401_UNAUTHORIZED
            )
