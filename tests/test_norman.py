from unittest import mock

import pytest
from norman.norman import DataInput


@pytest.fixture
def test_data():
    return {"order": 1, "settings": {"index": {"mapping": {"total_fields": {"limit": 10000}}, "refresh_interval": "5s"}}}

class TestDataInput:
    def test_data_input(self, test_data):
        d = DataInput(test_data)
        assert d.flat == {'order': 1, 'settings.index.mapping.total_fields.limit': 10000, 'settings.index.refresh_interval': '5s'}

