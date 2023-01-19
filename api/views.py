from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *


# view for registering users
class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url 
    permission_classes = (AllowAny,)
    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# edit required .
class ProviderAPIView(mixins.CreateModelMixin,generics.ListAPIView): # create list 
    permission_classes = [IsAuthenticated]
    serializer_class = ProviderSerializer

    def get_queryset(self):
        qs = Provider.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class ProviderDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProviderSerializer
    
    queryset = Provider.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request, *args, **kwargs)

class BankAPIView(mixins.CreateModelMixin, generics.ListAPIView): # create list 
    permission_classes = [IsAuthenticated]
    serializer_class = BankSerializer

    def get_queryset(self):
        qs = Bank.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs

    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class BankDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BankSerializer
    
    queryset = Bank.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request, *args, **kwargs)


class BankAccountAPIView(mixins.CreateModelMixin, generics.ListAPIView): # create list 
    permission_classes = [IsAuthenticated]
    serializer_class = BankAccountreadonlySerializer

    def get_queryset(self):
        qs = BankAccount.objects.all()
        query = self.request.GET.get('q')

        if query is not None:
            qs = qs.filter(content__icontains = query)
        return qs
    # does not support .create on nested serlizer so wwrited inow serlizer
    # def post(self,request,*args,**kwargs):
    #    return self.create(request,*args,**kwargs)
    # def post(self,request,*args,**kwargs):
    #     self.object = self.get_object()
    #     return super().post(request, *args, **kwargs)


class BankAccountCreateAPIView(generics.ListCreateAPIView): # create list 
    permission_classes = [IsAuthenticated]
    serializer_class = BankAccountSerializer
    
    queryset = BankAccount.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = BankAccountSerializer(queryset, many=True)
        return Response(serializer.data)


class BankAccountDetailAPIView(mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BankAccountSerializer
    
    queryset = BankAccount.objects.all()

    def put(self, request, *args, **kwargs):
        return  self.update(request,*args,**kwargs)
    
    def patch(self, request, *args, **kwargs):
        return  self.partial_update(request,*args,**kwargs)

    def delete(self, request, *args, **kwargs):
        return  self.destroy(request,*args,**kwargs)
