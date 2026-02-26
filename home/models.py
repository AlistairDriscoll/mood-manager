from django.db import models
from django.contrib.auth.models import User


class MoodEntry(models.Model):
    # Kaggle rows: user = None
    # Real user submissions: user = that user
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="mood_entries",
    )

    # Numeric fields (stored as decimals for consistent precision)
    sleep_hours = models.DecimalField(max_digits=6, decimal_places=3)
    screen_time = models.DecimalField(max_digits=6, decimal_places=3)
    exercise_minutes = models.DecimalField(max_digits=8, decimal_places=3)

    daily_pending_tasks = models.PositiveSmallIntegerField()

    interruptions = models.DecimalField(max_digits=6, decimal_places=3)
    fatigue_level = models.DecimalField(max_digits=6, decimal_places=3)
    social_hours = models.DecimalField(max_digits=6, decimal_places=3)
    coffee_cups = models.DecimalField(max_digits=5, decimal_places=2)

    # Categoricals
    DIET_CHOICES = [
        ("poor", "Poor"),
        ("average", "Average"),
        ("good", "Good"),
    ]
    diet_quality = models.CharField(max_length=10, choices=DIET_CHOICES)

    WEATHER_CHOICES = [
        ("sunny", "Sunny"),
        ("rainy", "Rainy"),
        ("cloudy", "Cloudy"),
        ("snowy", "Snowy"),
        ("hail", "Hail"),
        ("foggy", "Foggy"),
    ]
    weather = models.CharField(max_length=10, choices=WEATHER_CHOICES)

    # Outcomes / targets
    mood_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        who = self.user.username if self.user else "dataset"
        return f"{who}: mood {self.mood_score}, stress {self.stress_level}"
