from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("predict/", views.predict_view, name="predict"),
    path("improve-mood/", views.improve_my_mood, name="improve_mood"),
    path("reduce-stress/", views.reduce_stress, name="reduce_stress"),
    path("model-overview/", views.model_overview, name="model_overview"),
]
