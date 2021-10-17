from django.shortcuts import render
from django.http import JsonResponse
from  rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


class printName(APIView):
    def get(self,request):
        mesg=request.GET.get('value',None)
        if(mesg!=None):
            return Response("You have entered " + mesg)
        else:
            return Response("Something went wrong")



