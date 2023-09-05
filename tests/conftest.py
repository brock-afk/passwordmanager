import pytest
import tempfile


@pytest.fixture
def vaults_directory():
    with tempfile.TemporaryDirectory() as directory:
        yield directory
