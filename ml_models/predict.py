from pathlib import Path
import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
MOOD_PATH = BASE_DIR / "predicting_mood_score_linear_regression_model.pkl"
STRESS_PATH = BASE_DIR  / "predicting_stress_level_linear_regression_model.pkl"

mood_pipeline = joblib.load(MOOD_PATH)
stress_pipeline = joblib.load(STRESS_PATH)

FEATURES = [
    "sleep_hours",
    "screen_time",
    "exercise_minutes",
    "daily_pending_tasks",
    "interruptions",
    "fatigue_level",
    "social_hours",
    "coffee_cups",
    "diet_quality",
    "weather",
]

def clamp(x, lo=0.0, hi=10.0):
    return max(lo, min(hi, float(x)))

def predict_mood_and_stress(cleaned_data: dict) -> dict:
    # Build a single-row DF in the correct column order/names
    row = {k: cleaned_data[k] for k in FEATURES}
    X = pd.DataFrame([row], columns=FEATURES)

    mood = mood_pipeline.predict(X)[0]
    stress = stress_pipeline.predict(X)[0]

    # clamp to 1-10 range
    mood = clamp(mood, 1.0, 10)
    stress = clamp(stress, 1.0, 10)

    return {"mood_pred": mood, "stress_pred": stress}