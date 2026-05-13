import pytest
from main import BooksCollector

@pytest.fixture
def b_collector():
    return BooksCollector()