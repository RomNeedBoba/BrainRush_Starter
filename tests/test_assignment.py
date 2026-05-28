import subprocess, os

def test_notebook_runs():
    # Execute the notebook end-to-end; fails if any cell errors
    result = subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute",
         "--output", "executed.ipynb", "assignment.ipynb"],
        capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr

def test_csv_exists():
    assert os.path.exists("data.csv")