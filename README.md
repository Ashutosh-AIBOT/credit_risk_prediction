# Credit Risk Prediction

Banking risk intelligence with explainable classification models.

## Recommended GitHub Repo Name

enterprise-credit-risk-intelligence

## Domain

Retail banking and underwriting

## Objective

Predict probability of loan default using applicant profile and credit behavior.

## Business Value

Improves approval quality, lowers default losses, and supports policy-level risk governance.

## Dataset

Inferred Kaggle: https://www.kaggle.com/competitions/home-credit-default-risk

## Run Locally

conda run -n ml-env streamlit run app.py

## Dashboard Features

- Executive overview and business framing
- Prediction Center (single input + batch CSV)
- Model ranking leaderboard
- Model registry (all discovered model artifacts)
- Charts gallery (auto-load from charts/)
- Notebook traceability panel

## Notebook Path Setup

Inside notebooks:

from path_setup import BASE, RAW, PROCESSED, MODELS, CHARTS, load_raw_csv

Project path helpers:

- path_utils.py
- notebooks/path_setup.py
## Deploy on Render

This repo includes render.yaml. Connect repo in Render and deploy.

Start command used:

streamlit run app.py --server.port $PORT --server.address 0.0.0.0

## Git LFS

Large assets are tracked with Git LFS (models, charts, data artifacts).
