from array import array
from bdb import effective

from django.shortcuts import render, redirect
from .forms import UserHistoryForm
from .models import UserHistory

# Create your views here.
def solve(request):
    if request.method == 'POST':
        form = UserHistoryForm(request.POST)
        if form.is_valid():
            bmr = int()
            eff_weight = int()
            age = form.cleaned_data['age']
            height = form.cleaned_data['height']
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            user_ids = request.user.id
            if gender == 'male':
                bmr = 10 * weight + 6.25 * height - 5 * age + 5
            else:
                bmr = 10 * weight + 6.25 * height - 5 * age - 161
            imt = weight / ((height / 100) * (height / 100))
            if gender == 'male':
                eff_weight = height - 100 - ((height - 150)/4)
            else:
                eff_weight = height - 100 - ((height - 150)/2)
            prot = bmr*0.15/4
            fats = bmr*0.25/9
            hydra = (bmr - prot*4 - fats*9)/4
            zapros = UserHistory(user_id = int(user_ids), age = age, height = height, weight = weight, gender =gender,bmr = bmr, body_mass_index = imt, effectiv_weight = eff_weight, protein=prot, fats=fats, carbohydrates=hydra)
            zapros.save()
            return redirect('history/')
    form = UserHistoryForm
    return render (request, 'main/solve.html', {'form':form})
def history(request):
    form = UserHistory.objects.all().order_by('-date')
    array1 = []
    for el in form:
        if el.user_id == int(request.user.id):
            array1.append(el)
    return render(request, 'main/history.html', {'form':array1})

