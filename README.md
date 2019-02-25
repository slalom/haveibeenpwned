# Requirements
- Python 3.x
- pipenv

# Instalation

`pipenv install --dev`

# Input
The input is a CSV file containing the header and email addresses. See sample.csv for an example

# Usage

`pipenv run python run.py <file>`

*file* - CSV file with email addresses

e.g. `pipenv run python run.py sample.csv`

# Output

The script returns results in the standard output. To save results to a file, use the pipe syntax:

`... > output.csv`

The output is in the following format:

`<email>, <breach titile>, <breach date>`

It is possible to receive multiple lines per email (one for each breach).