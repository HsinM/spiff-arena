"""APIs for dealing with process groups, process models, and process instances."""
from flask.wrappers import Response


def test_raise_error() -> Response:
    raise Exception("This exception was generated by /debug/test-raise-error for testing purposes. Please ignore.")