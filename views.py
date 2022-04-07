from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action

from . models import student
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.authentication import SessionAuthentication

from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated, DjangoModelPermissions, \
    IsAuthenticatedOrReadOnly

from .serializers import studentSerializer


@api_view(['GET','POST','PATCH'])#from here we can allow the method we can call from postman
def get_home(request):
    if request.method=='GET':
        return  Response({'status':200,'message':'working properly','method_called':'GET'})

    elif request.method=='POST':
        return Response( {'status': 200, 'message': 'yes!n django is  working' ,'method_called':'POST'} )

    elif request.method=='PATCH':
        return Response( {'status': 200, 'message': 'yes!n django is  working' ,'method_called':'PATCH'} )

    else:
        return Response( {'status': 400, 'message': 'yes!n django is   working', 'method_called': 'invalid'} )





class studentList(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self, request):
      data=student.objects.all()
      #throttle_classes = [ScopedRateThrottle]
      #throttle_scope = 'modifystu'
      serializer = studentSerializer( data, many=True )
      return Response( {'status': True, 'message': 'todo-fetched', 'data': serializer.data} )

    def post(self, request):
        try:
            data = request.queryset
            data['user'] = request.user.id
            serializer = studentSerializer( data=data )
            if serializer.is_valid():
                serializer.save()
                print( serializer.data )

                return Response( {'status': True, 'data': serializer.data, 'message': 'sucess todo created'} )



            return Response( {'status': False,'data':serializer.errors, 'message': 'invalid data'} )

        except Exception as e :
           print(e)
        return Response( {'status': False, 'message': 'invalid data'} )

    def patch(self,request):
      try:
         data=request.data
         if not data.get('uid'):
            return Response({'status': False, 'message': 'uid is required', 'data':{}})

         obj=student.objects.get(uid=data.get('uid'))
         serializer=studentSerializer(obj,data=data,partial=True)
         if serializer.is_valid():
           serializer.save()
           return Response( {'status': True, 'data': serializer.data, 'message': 'sucess todo created'} )

         return Response( {'status': False, 'data': serializer.errors, 'message': 'invalid data'} )

      except Exception as e:
        print( e )

        return Response( {'status': False, 'message': 'invalid data'} )

