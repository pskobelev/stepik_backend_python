from uuid import uuid4

from django.http import JsonResponse, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
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
        tokens_id = list(t.token_id for t in (Token.objects.all()))
        try:
            if request.GET["token"] and request.GET["token"] in tokens_id:
                return Response(
                    GoodsSerializer(
                        Good.objects.all().values(), many=True
                    ).data,
                    status=HTTP_200_OK,
                )
            else:
                return HttpResponse(
                    "Token is invalid", status=HTTP_401_UNAUTHORIZED
                )
        except KeyError:
            return HttpResponse(
                "Token must be present", status=HTTP_401_UNAUTHORIZED
            )

    def post(self, request):
        tokens_id = list(t.token_id for t in (Token.objects.all()))

        if (
            request.GET.get("token", False)
            and request.GET.get("token", False) in tokens_id
        ):
            new = GoodsSerializer(data=request.data)
            if new.is_valid():
                new.save()
                return Response("Add", status=status.HTTP_201_CREATED)
        elif request.GET.get("token", False):
            return HttpResponse("Wrong token", status=HTTP_401_UNAUTHORIZED)
        else:
            return HttpResponse("Need token", status=HTTP_401_UNAUTHORIZED)
