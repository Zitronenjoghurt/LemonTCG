#!/bin/bash

set -e

echo "Clearing old builds..."
rm -rf dist/

echo "Building the package..."
python setup.py sdist bdist_wheel

echo "Uploading the package to PyPI..."
twine upload dist/*

echo "Done."