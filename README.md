# Progree Task 3 — CI/CD Pipeline

[![CI/CD Pipeline](https://github.com/Awan/progree-task3-cicd-pipeline/actions/workflows/ci.yml/badge.svg)](https://github.com/Awan/progree-task3-cicd-pipeline/actions/workflows/ci.yml)

A multi-stage automated CI/CD deployment pipeline built with GitHub Actions to demonstrate automated code validation, artifact generation, deployment, and execution metrics.

## Objective

Implement a robust CI/CD workflow that automatically validates application changes, builds a deployable Python package, transfers the build artifact between pipeline stages, and reports deployment results through GitHub Actions.

## Pipeline Workflow

The pipeline executes the following stages sequentially:

1. **Checkout** — Retrieves the application source code.
2. **Environment Setup** — Configures Python 3.12 on the GitHub-hosted runner.
3. **Dependency Installation** — Installs the project and required development tools.
4. **Static Linting** — Runs Ruff to detect code quality and style issues.
5. **Unit Testing** — Runs the pytest test suite.
6. **Build** — Creates Python source and wheel distribution packages.
7. **Artifact Management** — Uploads the validated build artifact for use by the deployment stage.
8. **Deployment** — Downloads the artifact and executes a deployment demonstration.
9. **Metrics** — Publishes deployment status, environment, runner, artifact, and commit information to the GitHub Actions job summary.

## Pipeline Jobs

```text
Static Linting
      ↓
Unit Tests
      ↓
Build Application
      ↓
Deploy Application
  └─ Deployment Metrics
```

The deployment stage runs only for successful pushes to the `main` branch. Pull requests run through linting, testing, and build validation without performing the deployment stage.

## Triggers

The workflow runs automatically for:

* Pushes to `main`
* Pull requests targeting `main`

## Build Artifacts

The build stage produces:

* Python source distribution (`.tar.gz`)
* Python wheel (`.whl`)

The generated packages are uploaded as the `progree-cicd-package` GitHub Actions artifact and downloaded by the deployment stage.

## Deployment

This project uses a self-contained deployment demonstration rather than deploying to an external production environment.

The deployment stage:

* Downloads the validated build artifact.
* Lists the generated package files.
* Reports deployment completion.
* Publishes execution metrics to the GitHub Actions Step Summary.

This provides a reproducible demonstration of artifact-based deployment without requiring external infrastructure or credentials.

## Validation

The project is validated locally and in GitHub Actions using:

* **Ruff** — Static linting
* **pytest** — Unit testing
* **actionlint** — GitHub Actions workflow validation

The automated pipeline confirms that the application passes linting and unit tests before the build and deployment stages execute.

## Technology Stack

* Python 3.12
* pytest
* Ruff
* GitHub Actions
* Git
* setuptools
* Python build tooling

## Project Structure

```text
.
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── progree_cicd/
│       ├── __init__.py
│       └── app.py
├── tests/
│   └── test_app.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Task Outcome

The completed pipeline demonstrates a multi-stage automated CI/CD process with sequential validation, artifact-based deployment, and visible execution status metrics through GitHub Actions.
