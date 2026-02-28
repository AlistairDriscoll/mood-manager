def mood_suggestions(inputs: dict) -> list[str]:
    tips = []

    sleep = inputs.get("sleep_hours", 0)
    screen = inputs.get("screen_time", 0)
    exercise = inputs.get("exercise_minutes", 0)
    fatigue = inputs.get("fatigue_level", 0)
    coffee = inputs.get("coffee_cups", 0)
    diet = inputs.get("diet_quality")
    weather = inputs.get("weather")

    if sleep < 7:
        tips.append("You logged lower sleep — aim for 7–8 hours to support"
                    " mood stability.")

    if screen > 6:
        tips.append("High screen time can affect mood — try"
                    " a 30 minute screen break this evening.")

    if exercise < 30:
        tips.append("Exercise boosts serotonin — even a"
                    " 15 minute walk can lift mood.")

    elif exercise > 120:
        tips.append("Very high exercise can sometimes increase "
                    "fatigue — make sure you're recovering properly.")

    if fatigue >= 7:
        tips.append("High fatigue detected — prioritise rest"
                    " and avoid overloading your day.")

    if coffee >= 4:
        tips.append("High caffeine intake can worsen mood swings "
                    "— consider reducing by 1 cup tomorrow.")

    if diet == "poor":
        tips.append("Diet quality looks low — try adding one"
                    " whole-food meal today (protein + veg).")

    if weather in ["snowy", "rainy"]:
        tips.append("Low sunlight weather detected — try getting"
                    " outside briefly or increase indoor lighting.")

    if not tips:
        tips.append("Your inputs look balanced — focus on one"
                    " enjoyable activity today to reinforce positive mood.")

    return tips


def stress_suggestions(inputs: dict) -> list[str]:
    """
    Generate personalised stress-reduction suggestions
    based on user input data.
    """

    tips = []

    sleep = inputs.get("sleep_hours", 0)
    pending = inputs.get("daily_pending_tasks", 0)
    interruptions = inputs.get("interruptions", 0)
    fatigue = inputs.get("fatigue_level", 0)
    social = inputs.get("social_hours", 0)
    coffee = inputs.get("coffee_cups", 0)
    screen = inputs.get("screen_time", 0)
    diet = inputs.get("diet_quality")

    if sleep < 7:
        tips.append("Low sleep increases stress levels. "
                    "Aim for 7–8 hours tonight.")

    if pending >= 8:
        tips.append(
            "High task load detected. "
            "Choose 1 priority task and ignore the rest for now."
        )

    if interruptions >= 10:
        tips.append(
            "Frequent interruptions raise stress. "
            "Try a 25-minute focused block with notifications off."
        )

    if fatigue >= 6:
        tips.append(
            "Fatigue can amplify stress. "
            "Schedule a short recovery break today."
        )

    if social == 0:
        tips.append(
            "No social interaction logged. "
            "Even a short message to someone can reduce stress."
        )

    if coffee >= 4:
        tips.append(
            "High caffeine intake may increase anxiety. "
            "Reduce intake after midday."
        )

    if screen >= 8:
        tips.append(
            "High screen time detected. "
            "Take a 20–30 minute break away from devices."
        )

    if diet == "poor":
        tips.append(
            "Poor diet quality can affect stress resilience. "
            "Add one balanced meal today (protein + vegetables)."
        )

    if not tips:
        tips.append(
            "Stress markers look moderate. "
            "Try a 2-minute breathing exercise "
            "(inhale 4s, exhale 6s)."
        )

    return tips
