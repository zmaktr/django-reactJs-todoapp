from rest_framework.views import APIView
from . models import React
from rest_framework.response import Response
from . serilizers import ReactSerilizers 

class ReactView(APIView):
    
    serilizers_class = ReactSerilizers
    
    def get(self, request):
        detail = [ {"name" : text.name, "detail" : text.detail} for text in React.objects.all() ]
        return Response(detail)
    
    def post(self, request):
        serilizer = ReactSerilizers(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            serilizer.save()
            return Response(serilizer.data)



