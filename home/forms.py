# forms.py
from django import forms

WEATHER_CHOICES = [
    ("snowy", "Snowy"),
    ("sunny", "Sunny"),
    ("cloudy", "Cloudy"),
    ("rainy", "Rainy"),
]

DIET_CHOICES = [
    ("poor", "Poor"),
    ("average", "Average"),
    ("good", "Good"),
]

class PredictionForm(forms.Form):
    sleep_hours = forms.FloatField(min_value=0, max_value=24)
    screen_time = forms.FloatField(min_value=0, max_value=24)
    exercise_minutes = forms.FloatField(min_value=0, max_value=300)
    daily_pending_tasks = forms.IntegerField(min_value=0, max_value=100)
    interruptions = forms.IntegerField(min_value=0, max_value=100)
    fatigue_level = forms.FloatField(min_value=0, max_value=10)
    social_hours = forms.FloatField(min_value=0, max_value=24)
    coffee_cups = forms.IntegerField(min_value=0, max_value=20)

    diet_quality = forms.ChoiceField(choices=DIET_CHOICES)
    weather = forms.ChoiceField(choices=WEATHER_CHOICES)

    def clean_diet_quality(self):
        return self.cleaned_data["diet_quality"].strip().lower()

    def clean_weather(self):
        return self.cleaned_data["weather"].strip().lower()