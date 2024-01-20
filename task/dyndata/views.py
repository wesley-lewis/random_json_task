from rest_framework.response import Response
from rest_framework.views import APIView
from .models import DynData

class DataCollector(APIView):
    def post(self, request, *args, **kwargs):
        d = DynData(randomdata = request.data)
        d.save()
        return Response({"message": "success"})

    def get(self, request, *args, **kwargs):
        data = DynData.objects.all()

        arr = [d.randomdata for d in data]
        return Response({"data": arr})
