from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Signup,Department
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .serializers import TicketSerializers
from django.views import View


# class Login(View):
def login(request):
    return render(request, 'login.html')

    # def post(self,request):
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     return render(request, 'login.html')


def signup(request):
        print(request.method)
        if request.method == 'GET':
            return render(request, 'signup.html')
        else:
            postData = request.POST
            Name = postData.get('name')
            Email = postData.get('email')
            Phone_number = postData.get('phone')
            password = postData.get('password')
            Department.name = postData.get('Name')
            role = postData.get('Role')
            signup = Signup(Name=Name,
                            Email=Email,
                            Phone_number=Phone_number,
                            password=password,
                            Role=role
                            )
            department = Department(Name=Department.name)
            signup.save()
            department.save()
            return HttpResponse("successfully signup")



class TicketView(APIView):
    template_name = 'tickets.html'

    def get(self,request):
        # result = Ticket.objects.all()

        url = request.get("https://company.zendesk.com/api/v2/tickets/35436.json")
        serializer =TicketSerializers(url,many=True)
        return Response({"status":"success", "tickets" :serializer.data},status=200)




