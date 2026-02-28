from django.shortcuts import render
from .forms import PredictionForm
from ml_models.predict import predict_mood_and_stress


def index(request):
    """
    Return the index page
    """

    return render(request, "home/index.html")


def predict_view(request):
    mood_pred = None
    stress_pred = None

    if request.method == "POST":
        form = PredictionForm(request.POST)
        if form.is_valid():
            preds = predict_mood_and_stress(form.cleaned_data)
            mood_pred = preds["mood_pred"]
            stress_pred = preds["stress_pred"]
    else:
        form = PredictionForm()

    return render(
        request,
        "predict.html",
        {
            "form": form,
            "mood_pred": mood_pred,
            "stress_pred": stress_pred,
        },
    )


def improve_my_mood(request):

    return render(
        request,
        'improve_mood.html',
    )


def reduce_stress(request):

    return render(
        request,
        'reduce_stress.html',
    )


def contact(request):

    return render(
        request,
        'contact.html',
    )


def faq(request):

    return render(
        request,
        'faq.html',
    )