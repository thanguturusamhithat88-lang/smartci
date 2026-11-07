
def summarize_logs(log_content, errors, warnings):
    """
    Generates a summary of build/error logs.
    """

    total_lines = len(log_content.splitlines())

    summary = f"""
    BUILD LOG SUMMARY
    -----------------
    Total Log Lines: {total_lines}
    Total Errors: {len(errors)}
    Total Warnings: {len(warnings)}
    """

    if errors:
        summary += "\nErrors Found:\n"
        for error in errors:
            summary += f"- {error}\n"
    else:
        summary += "\nNo errors found.\n"

    if warnings:
        summary += "\nWarnings Found:\n"
        for warning in warnings:
            summary += f"- {warning}\n"
    else:
        summary += "\nNo warnings found.\n"

    return summary
