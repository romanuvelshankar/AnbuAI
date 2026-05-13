def detect_stress_level(mood_score):
    if mood_score < 4:
        return "High stress detected"
    else:
        return "Stress level normal"

print(detect_stress_level(3))
