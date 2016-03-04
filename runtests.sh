if [ "$LINT" ]; then
    flake8 html_json_forms tests --exclude migrations
else
    python setup.py test
fi
