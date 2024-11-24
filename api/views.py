from django.shortcuts import render
from rest_framework.views import APIView
from api.models import Property
from rest_framework.response import Response
from api.serializers import PropertySerializer,SignUpSerializer
from rest_framework import authentication,permissions
from django.contrib.auth.models import User

# Create your views here.

class PropertyCreateList(APIView):

    serializer_class=PropertySerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        qs=Property.objects.all()

        if "propert_items" in request.query_params:

            filter_text=request.query_params.get("property_type")

            qs=qs.filter(property_type=filter_text)

        serializer_instance=self.serializer_class(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data) 

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data) 

        return Response(data=serializer_instance.errors)      

class PropertyRetrieveUpdateDestroyView(APIView):

    serializer_class=PropertySerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Property.objects.get(id=id)

        serializer_instance=self.serializer_class(qs)

        return Response(data=serializer_instance.data)

    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Property.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})    


    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        property_object=Property.objects.get(id=id)

        serializer_instance=self.serializer_class(data=request.data,instance=property_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)    

        return Response(data=serializer_instance.errors)    


class PropertyTypeListview(APIView):

    serializer_class=PropertySerializer

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    def get(self,request,*args,**kwargs):

        property_types=[tp[0] for tp in Property.PROPERTY_CHOICES]

        return Response(data=property_types)


class SignUpView(APIView):

    serializer_class=SignUpSerializer

    def post(self,request,*args,**kwargs):

        serializer_instance=self.serializer_class(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)

        return Response(data=serializer_instance.errors)    



