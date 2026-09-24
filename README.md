# Progree Task 3 — CI/CD Pipeline

A multi-stage automated CI/CD deployment pipeline built with GitHub Actions.

## Objective

Demonstrate an automated workflow that validates application changes on remote pushes and pull requests, performs static analysis and unit testing, builds an application artifact, and executes a deployment stage with visible execution status metrics.

## Pipeline Stages

1. Checkout source code
2. Set up Python
3. Install project dependencies
4. Run Ruff static linting
5. Run pytest unit tests
6. Build the application artifact
7. Deploy the validated artifact
8. Publish execution status and deployment metrics

## Technology

- Python
- pytest
- Ruff
- GitHub Actions
- Git
