if [ "$LINT" ]; then
    flake8 html_json_forms tests
else
    python setup.py test
fi
