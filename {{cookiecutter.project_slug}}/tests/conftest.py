"""
Pytest configuration and fixtures for {{ cookiecutter.project_name }}.

This module provides common test fixtures and configuration for the test suite.
"""

import sys
from pathlib import Path

import pytest

# Add src directory to Python path for imports
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))


@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return {
        "test_string": "sample",
        "test_number": 42,
        "test_list": [1, 2, 3],
    }


@pytest.fixture
def temp_file(tmp_path):
    """Create a temporary file for testing."""
    file_path = tmp_path / "test_file.txt"
    file_path.write_text("test content")
    return file_path


@pytest.fixture
def mock_config():
    """Provide mock configuration for testing."""
    return {
        "debug": False,
        "log_level": "INFO",
        "max_retries": 3,
    }
