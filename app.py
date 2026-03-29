import os

from dashboard_core import ProjectConfig, run_project_app


CONFIG = ProjectConfig(
    key="Project 01",
    title="Credit Risk Prediction",
    subtitle="Banking risk intelligence with explainable classification models",
    icon="🏦",
    domain="Retail banking and underwriting",
    objective="Predict probability of loan default using applicant profile and credit behavior.",
    business_value="Improves approval quality, lowers default losses, and supports policy-level risk governance.",
    prediction_label="Credit Risk",
    highlights=[
        "Built a multi-model credit risk stack with leaderboard-driven model selection.",
        "Supports high-volume batch scoring workflow for portfolio-level underwriting.",
        "Promotes explainable decisions through benchmark transparency and model traceability.",
        "Designed production-friendly UX with reusable prediction pipelines.",
        "Demonstrates business framing from model metrics to risk reduction outcomes.",
    ],
)


run_project_app(CONFIG, os.path.dirname(__file__))
