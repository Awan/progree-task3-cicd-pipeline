import pytest

from progree_cicd.app import build_status, health_check


def test_build_status_returns_deployment_metadata():
    result = build_status("progree-app", "1.0.0")

    assert result == {
        "service": "progree-app",
        "version": "1.0.0",
        "status": "ready",
    }


def test_build_status_rejects_empty_service():
    with pytest.raises(ValueError, match="service must not be empty"):
        build_status("", "1.0.0")


def test_build_status_rejects_empty_version():
    with pytest.raises(ValueError, match="version must not be empty"):
        build_status("progree-app", "")


def test_health_check_returns_healthy():
    assert health_check() == "healthy"
