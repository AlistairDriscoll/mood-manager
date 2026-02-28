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
