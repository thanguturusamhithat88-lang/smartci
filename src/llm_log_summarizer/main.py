
from log_reader import read_log_file
from error_detector import detect_errors
from llm_summarizer import summarize_logs

# Read the sample log file
log_content = read_log_file("src/llm_log_summarizer/sample_logs/build.log")

if log_content:
    # Detect errors and warnings
    errors, warnings = detect_errors(log_content)

    # Generate summary
    summary = summarize_logs(log_content, errors, warnings)

    # Display final result
    print(summary)
else:
    print("Unable to read log file.")
