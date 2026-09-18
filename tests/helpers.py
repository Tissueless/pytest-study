def assert_status(response, expected_status):
    assert response.status_code == expected_status

def assert_json_response(response):
    assert "application/json" in response.headers["Content-Type"]

def assert_required_fields(data, fields):
    for field in fields:
        assert field in data

def assert_response_data(data, expected_data):
    for key, expected_value in expected_data.items():
        assert data[key] == expected_value

def assert_success_json_response(response, expected_status=200):
    assert_status(response, expected_status)
    assert_json_response(response)

def assert_field_types(data, expected_types):
    for field, expected_type in expected_types.items():
        assert isinstance(
            data[field],
            expected_type
        ), f"{field} should be {expected_type.__name__}, but got {type(data[field]).__name__}"

def assert_fields_exist(data, expected_fields):
    for field in expected_fields:
        assert field in data, f"{field} field is missing"

def assert_schema(data, schema):
    assert_fields_exist(data, schema.keys())
    assert_field_types(data, schema)