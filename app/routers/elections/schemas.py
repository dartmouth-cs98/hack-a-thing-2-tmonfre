from flask import request, jsonify
from functools import wraps
from voluptuous import Any, Schema, Required, Optional, MultipleInvalid, Invalid

sample_schema = Schema({
    Required('id'): int,
})


def validate_json(f):
    @wraps(f)
    def wrapper(*args, **kw):
        try:
            request.json
        except Exception:
            msg = "payload must be a valid json"
            return jsonify({"error": msg}), 400
        return f(*args, **kw)
    return wrapper


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            try:
                schema_name(request.json)
            except (Invalid, MultipleInvalid) as e:
                return jsonify({"error": str(e)}), 400
            return f(*args, **kw)
        return wrapper
    return decorator
