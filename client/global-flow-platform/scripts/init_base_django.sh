#!/bin/bash

echo "Going up one directory..."
cd ..

echo "Starting the Django project 'manager'..."
uv run django-admin startproject manager .

echo "Done. Project should be created in the directory you were just in."
# Optional: Go back to the original directory
# cd - > /dev/null