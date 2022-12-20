from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from app.utils import *



class SendFile(APIView):
    def post(self,request):
        try:
            data = request.data 
            email = data['email']
            subject = 'resume pdf'
            message = "this is your resume file"
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                SendEmail(email=email,subject=subject,message=message).start()
                return Response(
                    {
                        'status' : 200,
                        'message' : 'request successful... check email'
                    }
                )

            return Response(
                    {
                        'status' : 400,
                        'message' : 'Somethimg went wrong ',
                        'data': serializer.errors,

                    }
                )



        except Exception as w:
            return Response(str(w))