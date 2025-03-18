import mlflow
from dagshub import dagshub_auth

# Authenticate with DagsHub
dagshub_auth.login("cleavestone", "9a6fd44eeb938b96d9e0cf88e3dca0850991490a")

# Set MLflow tracking URI to DagsHub
mlflow.set_tracking_uri("https://dagshub.com/cleavestone/customer-churn-mlops.mlflow")

print("MLflow is now tracking on DagsHub!")