"""Core application logic for the Progree CI/CD demonstration project."""


def build_status(service: str, version: str) -> dict[str, str]:
    """Return deployment metadata for a service."""
    if not service.strip():
        raise ValueError("service must not be empty")

    if not version.strip():
        raise ValueError("version must not be empty")

    return {
        "service": service,
        "version": version,
        "status": "ready",
    }


def health_check() -> str:
    """Return the application's health status."""
    return "healthy"
