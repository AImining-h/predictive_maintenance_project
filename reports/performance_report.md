# 📊 Mining Truck Failure Prediction – Performance Report

## ✅ Model Performance Summary
- Accuracy: **0.86**
- F1 Score: **0.55**

## 🔍 Confusion Matrix
[[15547, 1430], [1344, 1679]]

- **[TN, FP]** = No failure predicted, actual = no/failure
- **[FN, TP]** = Failure predicted, actual = no/failure

## 🧠 Top 5 Important Features (XGBoost)
- last_maintenance_days: 0.7193
- vibration_level: 0.2580
- load_weight: 0.0059
- oil_pressure: 0.0058
- engine_temp: 0.0057

## 🛠 Suggestions for Improvement
- 🔁 Try tuning classification threshold (e.g., >0.4 instead of 0.5).
- 📊 Collect more failure samples to reduce class imbalance.
- 🧪 Explore time-based features (like rate of change in vibration).
- 🎯 Use SHAP per-row plots to investigate false positives/negatives.
