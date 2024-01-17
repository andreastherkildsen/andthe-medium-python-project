#!/bin/bash

# Remove Python cache files from src directory
find ../src -type f -name "*.pyc" -delete

# Remove Python cache files from tests directory
find ../tests -type f -name "*.pyc" -delete

echo "Python cache files removed from src and tests directories."