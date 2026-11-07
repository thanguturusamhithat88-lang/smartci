
# Build-Failure Prediction

## 1. Introduction
Build-Failure Prediction is a Python-based project
that analyzes build logs and predicts possible
build failures using errors and warnings.

## 2. Objectives
- Read build log files.
- Detect errors and warnings.
- Predict build failure risks.
- Display prediction results.

## 3. Technologies Used
- Python
- VS Code
- Git and GitHub
- Pytest

## 4. Project Structure
src/build_failure_prediction/
- __init__.py
- log_reader.py
- error_detector.py
- failure_predictor.py
- main.py
- sample_logs/build.log

## 5. Implementation
1. Read build logs.
2. Detect errors and warnings.
3. Analyze detected issues.
4. Predict build status.
5. Display results.

## 6. Testing
Automated testing was performed using Pytest.

Result: 5 test cases passed successfully.

## 7. Execution
Run the project using:

python -m src.build_failure_prediction.main

Run tests using:

python -m pytest tests/test_build_failure_prediction.py -v

## 8. Conclusion
The project successfully reads build logs,
detects errors and warnings, and predicts
possible build failures using rule-based logic.
