
import subprocess
import sys

# Get changed files from the previous commit
def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "origin/main"],
        capture_output=True,
        text=True
    )

    return result.stdout.splitlines()


# Select tests based on changed files
def select_tests(changed_files):
    selected_tests = set()

    for file in changed_files:
        if "__pycache__" in file or file.endswith(".pyc"):
            continue

        if file.startswith("src/"):
            module = file.split("/")[-1].replace(".py", "")
            test_file = f"tests/test_{module}.py"
            selected_tests.add(test_file)

    return sorted(selected_tests)


# Run selected tests
def run_tests(tests):
    if not tests:
        print("No related tests found.")
        return

    command = [sys.executable, "-m", "pytest"] + tests

    print("Running selected tests:")
    print(tests)

    subprocess.run(command, check=True)


if __name__ == "__main__":
    changed_files = get_changed_files()

    print("Changed files:")
    print(changed_files)

    tests = select_tests(changed_files)

    run_tests(tests)
