from django.shortcuts import render , redirect
# from .forms import DataForm
# from .models import Data
from joblib import load


def home(request):
    return render(request , 'index.html')  

loaded_model = load('ML_model/random_forest_model.joblib')
loaded_le = load('ML_model/label_encoder.joblib')


def crop(request):
    if request.method == "POST":
        N = request.POST.get('nitrogen')
        P = request.POST.get('phosphorous')
        K = request.POST.get('potassium')
        temp = request.POST.get('temperature')
        humid = request.POST.get('humidity')
        ph = request.POST.get('ph')
        rain = request.POST.get('rainfall')
        
        input_data = [[N, P, K, temp, humid, ph, rain]]
        prediction_encoded = loaded_model.predict(input_data)
        prediction_original = loaded_le.inverse_transform(prediction_encoded)
        prediction = prediction_original[0]
        
        print(N, P, K, temp, humid, ph, rain, prediction)
        
        context = {
            "N": N,
            "P": P,
            "K": K,
            "temp": temp,
            "humid": humid,
            "ph": ph,
            "rain": rain,
            "prediction": prediction
        }
        request.session['crop_context'] = context

        return redirect('crop_results')
    
    return render(request, 'index.html')


def crop_results(request):
    context = request.session.get('crop_context', {})

    
    return render(request, 'crop-results.html' , context)
