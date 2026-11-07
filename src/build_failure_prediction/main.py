
from src.build_failure_prediction.log_reader import read_log_file
from src.build_failure_prediction.error_detector import detect_errors
from src.build_failure_prediction.failure_predictor import predict_failure

# Read the build log
log_file = "src/build_failure_prediction/sample_logs/build.log"

log_content = read_log_file(log_file)

if log_content:

    # Detect errors and warnings
    errors, warnings = detect_errors(log_content)

    # Predict build result
    prediction, reason = predict_failure(errors, warnings)

    # Display results
    print("\n===== BUILD FAILURE PREDICTION =====")

    print("Total Log Lines:", len(log_content.splitlines()))
    print("Total Errors:", len(errors))
    print("Total Warnings:", len(warnings))

    print("\nPrediction:", prediction)
    print("Reason:", reason)

    if errors:
        print("\nErrors Found:")
        for error in errors:
            print("-", error)

    if warnings:
        print("\nWarnings Found:")
        for warning in warnings:
            print("-", warning)

else:
    print("Unable to read build log file.")
