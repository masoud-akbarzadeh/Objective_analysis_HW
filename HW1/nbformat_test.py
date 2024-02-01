import nbformat
from nbformat.validator import validate, NotebookValidationError

notebook_filename = 'HW1_3.ipynb'  # replace with your file name

with open('HW1_3.ipynb') as notebook_file:
    notebook = nbformat.read(notebook_file, as_version=4)
    try:
        validate(notebook)
        print("Notebook is valid")
    except NotebookValidationError as e:
        print("Notebook validation failed: ", e)