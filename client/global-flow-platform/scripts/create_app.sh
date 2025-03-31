#!/bin/bash

# Check if the user provided an app name
if [ -z "$1" ]; then
  echo "Please provide an app name."
  echo "Usage: ./create_app.sh <your_app_name>"
  exit 1 # Exit because no name was given
fi

# Get the app name from the first argument ($1)
APP_NAME=$1

# Run the command with the provided app name
echo "Creating app: $APP_NAME"
uv run ../manage.py startapp "$APP_NAME"

echo "Done."
