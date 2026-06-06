prob = model.predict_proba(customer)[0][1]

print("Default Probability:", prob)
print("Risk Category:", calculate_risk_score(prob))
