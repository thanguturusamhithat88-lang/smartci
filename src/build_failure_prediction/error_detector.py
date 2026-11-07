
def detect_errors(log_content):
    """
    Identify errors and warnings from build logs.
    """

    errors = []
    warnings = []

    for line in log_content.splitlines():

        if "ERROR" in line.upper() or "FAILED" in line.upper():
            errors.append(line)

        elif "WARNING" in line.upper():
            warnings.append(line)

    return errors, warnings
