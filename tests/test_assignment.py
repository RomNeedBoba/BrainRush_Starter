<<<<<<< HEAD
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
=======
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
>>>>>>> b546c9aa6d8409e301c1cff07bf822c28966b6d1
    assert os.path.exists("data.csv")