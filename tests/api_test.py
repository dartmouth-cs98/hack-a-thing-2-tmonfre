import pytest
from flask import jsonify


class TestAPI:

    def test_route(self, testapp):
        response = testapp.get('/')
        response_data = response.json
        assert response_data['code'] == 200
        assert response_data['message'] == "SUCCESS"
