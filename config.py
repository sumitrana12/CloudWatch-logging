import os

# Core environment variables
APP_NAME = os.getenv("APP_NAME", "app-wf-poc")
ENV = os.getenv("APP_ENV", "dev")  # dev, staging, prod

# Derived settings
LOG_GROUP_NAME = f"{APP_NAME}-{ENV}"
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")

