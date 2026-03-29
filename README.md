# Credit Risk Prediction

## Dashboard

Run with:

conda run -n ml-env streamlit run 01_credit_risk_prediction/app.py

## Dataset

Inferred Kaggle: https://www.kaggle.com/competitions/home-credit-default-risk

## App Features

- Executive overview with business objective and model summary
- Prediction center (single record + batch CSV)
- Model benchmark and ranking system
- Model registry page showing all discovered model artifacts in `models/`
- Charts gallery from `charts/`
- Notebook traceability from `notebooks/`
- Recruiter-impact highlights

## Notebook Path Setup (Global)

Use this inside notebooks:

```python
from path_setup import BASE, RAW, PROCESSED, MODELS, CHARTS, load_raw_csv

df = load_raw_csv("application_train.csv")
```

Shared path utility file:

- `path_utils.py` (project root)
- `notebooks/path_setup.py` (notebook helper)

## Standalone Deployment

This project contains its own `dashboard_core.py` and `app.py` for independent hosting.
