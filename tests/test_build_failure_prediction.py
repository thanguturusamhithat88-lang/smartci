
from src.build_failure_prediction.error_detector import detect_errors
from src.build_failure_prediction.failure_predictor import predict_failure


def test_build_failure():
    errors = ["ERROR: Missing dependency"]
    warnings = []

    prediction, reason = predict_failure(errors, warnings)

    assert prediction == "BUILD FAILURE"


def test_high_risk():
    errors = []
    warnings = ["WARNING 1", "WARNING 2", "WARNING 3"]

    prediction, reason = predict_failure(errors, warnings)

    assert prediction == "HIGH RISK"


def test_low_risk():
    errors = []
    warnings = ["WARNING: Deprecated library"]

    prediction, reason = predict_failure(errors, warnings)

    assert prediction == "LOW RISK"


def test_build_success():
    errors = []
    warnings = []

    prediction, reason = predict_failure(errors, warnings)

    assert prediction == "BUILD SUCCESS LIKELY"


def test_error_detection():
    log = """
    Build started
    ERROR: Missing dependency
    WARNING: Deprecated library
    """

    errors, warnings = detect_errors(log)

    assert len(errors) == 1
    assert len(warnings) == 1
