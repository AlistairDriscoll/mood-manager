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
    sleep_hours = forms.FloatField(
        min_value=0,
        max_value=12,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "0.1",
            "min": "0",
            "max": "12"
        })
    )
    
    screen_time = forms.FloatField(
        min_value=0, max_value=16,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "0.1",
            "min": "0",
            "max": "16"
        })
    )

    # Sliders: use RangeInput + bootstrap form-range
    exercise_minutes = forms.FloatField(
        min_value=0, max_value=180,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "10",
            "min": "0",
            "max": "180"
        })
    )

    daily_pending_tasks = forms.IntegerField(
        min_value=0, max_value=20,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "1",
            "min": "0",
            "max": "20"
        })
    )
    interruptions = forms.IntegerField(
        min_value=0, max_value=30,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "1",
            "min": "0",
            "max": "30"
        })
    )
    fatigue_level = forms.FloatField(
        min_value=0, max_value=10,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "0.1",
            "min": "0",
            "max": "10"
        })
    )
    social_hours = forms.FloatField(
        min_value=0, max_value=10,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "0.1",
            "min": "0",
            "max": "10"
        })
    )
    coffee_cups = forms.IntegerField(
        min_value=0, max_value=10,
        widget=forms.NumberInput(attrs={
            "type": "range",
            "class": "form-range",
            "step": "1",
            "min": "0",
            "max": "10"
        })
    )

    diet_quality = forms.ChoiceField(
        choices=DIET_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )
    weather = forms.ChoiceField(
        choices=WEATHER_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    def clean_diet_quality(self):
        return self.cleaned_data["diet_quality"].strip().lower()

    def clean_weather(self):
        return self.cleaned_data["weather"].strip().lower()