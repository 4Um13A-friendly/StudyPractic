from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
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
from .models import CustomUser, UserHistory, User
from .serializers import UserSerializer, UserHistorySerializer, UserRegistrationSerializer, UserHistoryReturnSerializer, UserHistoryReturnNowSerializer, EEUserSerializer
from rest_framework.permissions import IsAuthenticated

class UserAPIView(APIView):
    def post(self, request):
        print('asdasd')
        serializer = EEUserSerializer(data=request.data)
        print(serializer)
        serializer.is_valid()
        if True:
            arr = CustomUser.objects.all()
            flag = True

            if flag == True:
                #user = authenticate(username = serializer.validated_data['login'], password = serializer.validated_data['password'])
                #login(request, user)
                #print(request.user.id)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistreationAPIView(APIView):
    def post(self, request):
        print('Yes')
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.validated_data['login'])
            buf = User.objects.create(login = serializer.validated_data['login'], password = serializer.validated_data['password'])
            buf.save()
            users = User.objects.all()
            print(users)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.is_valid())
        print(serializer.errors)
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
            zapros = UserHistory(user_id=int(1), age=age, height=height, weight=weight, gender=gender, bmr=bmr,
                                 body_mass_index=imt, effectiv_weight=eff_weight, protein=prot, fats=fats,
                                 carbohydrates=hydra)
            zapros.save()
            # Сохраняем объект, если данные валидны
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Возвращаем ошибки валидации
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        print('asdasd')
        back = UserHistory.objects.all()
        data = back[0]
        serializer = UserHistoryReturnNowSerializer(data, many=False)
        print(data.bmr)
        return Response(serializer.data)

class UserHistoryReturnAPIView(APIView):
    def get(self, request):
        data = UserHistory.objects.all()
        arr = []
        for el in data:
            if el.user_id == request.user.id:
                arr.append(el)
        data = arr
        print(data)
        serializer = UserHistoryReturnSerializer(data, many=True)
        return Response (serializer.data)
