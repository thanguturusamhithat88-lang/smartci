
def predict_failure(errors, warnings):
    """
    Predict whether the build will succeed or fail.
    """

    if len(errors) > 0:
        prediction = "BUILD FAILURE"
        reason = "Errors detected in build logs."

    elif len(warnings) >= 3:
        prediction = "HIGH RISK"
        reason = "Multiple warnings detected."

    elif len(warnings) > 0:
        prediction = "LOW RISK"
        reason = "Some warnings detected."

    else:
        prediction = "BUILD SUCCESS LIKELY"
        reason = "No errors or warnings detected."

    return prediction, reason
