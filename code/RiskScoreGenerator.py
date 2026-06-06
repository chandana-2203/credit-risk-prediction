def calculate_risk_score(probability):
    if probability > 0.8:
        return "High Risk"

    elif probability > 0.5:
        return "Medium Risk"

    return "Low Risk"
