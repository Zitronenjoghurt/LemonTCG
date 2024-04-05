#!/bin/bash

set -e

echo "Clearing old builds..."
rm -rf dist/

echo "Building the package..."
python setup.py sdist bdist_wheel

echo "Done."