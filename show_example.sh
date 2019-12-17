coverage run -m pytest tests/
coverage report
echo "Showing results of .coverage file:\n"
cat .coverage
