from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserForm
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# def authterisation(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             flag = False
#             users = User.objects.all()
#             for el in users:
#                 if el.login == form.cleaned_data['login'] and el.password == form.cleaned_data['password']:
#                     flag = True
#             if (flag == True):
#                 return redirect('main/')
#     form = UserForm()
#     return render (request, 'login/login.html', {'form':form})

def registrations(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main/')
    form = UserForm()
    return render (request, 'login/registration.html', {'form':form})

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser, UserHistory
from .serializers import UserSerializer, UserHistorySerializer, UserRegistrationSerializer, UserHistoryReturnSerializer, \
    UserHistoryReturnNowSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# class UserAPIView(APIView):
#     def post(self, request):
#         print('asdasd')
#         serializer = EEUserSerializer(data=request.data)
#         print(serializer.initial_data)
#         print(serializer.is_valid())
#         #print(serializer.validated_data['login'])
#         #print(serializer.validated_data['password'])
#         #user = authenticate(username=serializer.initial_data.get('login'), password=serializer.initial_data.get('password'))
#         users = User.objects.all()
#         flag2 = False
#         #for i in users:
#             #if i.login == serializer.initial_data.get('login') and i.password == serializer.initial_data.get('password'):
#         print()
#         username = serializer.initial_data.get('login')
#         password = serializer.initial_data.get('password')
#         user = authenticate(username=username,
#                             password=password)
#         if user is not None:
#             flag2 = True
#             login(request, user)
#             print(request.user.id)
#
#         print(request.user.id)
#             #login(request, user)
#             #print(request.user.id)
#
#         if flag2 == True:
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class UserRegistreationAPIView(APIView):
#     def post(self, request):
#         print('Yes')
#         serializer = UserRegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             print(serializer.validated_data['login'])
#             buf = User.objects.create(login = serializer.validated_data['login'], password = serializer.validated_data['password'])
#             buf.save()
#             login(request, buf)
#             users = User.objects.all()
#             print(users)
#             print(request.user.id)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.is_valid())
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
ID_USER = int()
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        print(serializer)
        print(serializer.is_valid())
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self, request):
        logout(request)
        serializer = UserLoginSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            global ID_USER
            ID_USER = request.user.id
            print(request.user.is_authenticated)
            print(request.user.is_authenticated)
            print(request.user.is_authenticated)
            print(request.user.is_authenticated)
            print(request.user.id)
            print(request.user.id)
            print(request.user.id)
            print(request.user.id)
            print(request.user.id)
            print(request.session)
            print(request.session)
            print(request.session)
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        print(serializer)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
bmr = float()
body_mass = float()
eff = float()
prot = float()
fat = float()
hydra = float()
class UserHistoryCreateAPIView(APIView):
    def post(self, request):
        print('Yes')
        # Данные, отправленные клиентом, доступны в request.data
        serializer = UserHistorySerializer(data=request.data)
        print(serializer)
        # Проверяем валидность данных
        if serializer.is_valid():
            #bmr = int()
            eff_weight = int()
            age = int(serializer.validated_data['age'])
            height = int(serializer.validated_data['height'])
            weight = int(serializer.validated_data['weight'])
            gender = str(serializer.validated_data['gender'])
            user_ids = request.user.id
            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            imt = weight / ((height / 100) * (height / 100))
            if gender == 'male':
                eff_weight = height - 100 - ((height - 150) / 4)
            else:
                eff_weight = height - 100 - ((height - 150) / 2)
            prot = bmr * 0.15 / 4
            fats = bmr * 0.25 / 9
            hydra = (bmr - prot * 4 - fats * 9) / 4
            zapros = UserHistory(user_id=ID_USER, age=age, height=height, weight=weight, gender=gender, bmr=round(bmr, 2),
                                 body_mass_index=round(imt, 2), effectiv_weight=round(eff_weight, 2), protein=round(prot, 2), fats=round(fats, 2),
                                 carbohydrates=round(hydra, 2))
            zapros.save()
            # Сохраняем объект, если данные валидны
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Возвращаем ошибки валидации
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        print('asdasd')
        back = UserHistory.objects.all()
        print(back)
        data = back[len(back) - 1]
        print (data)
        serializer = UserHistoryReturnNowSerializer(data, many=False)
        print(data.bmr)
        return Response(serializer.data)

class UserHistoryReturnAPIView(APIView):
    def get(self, request):
        print(request.session)
        print(request.session)
        print(request.session)
        print(request.session)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(request.user.id)
        print(ID_USER)
        data = UserHistory.objects.all()
        arr = []
        for el in data:
            if el.user_id == ID_USER:
                arr.append(el)

        data = arr#.reverse()
        data.reverse()
        print(data)
        serializer = UserHistoryReturnSerializer(data, many=True)
        return Response (serializer.data)
