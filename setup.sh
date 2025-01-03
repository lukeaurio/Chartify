#!/bin/bash

# Set up pyenv
if ! command -v pyenv &> /dev/null
then
    echo "pyenv could not be found, please install pyenv first."
    exit 1
fi

# Initialize pyenv
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

# Set Python version
# Check if Python is installed and set the version
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
else
    echo "Python is not installed. Please install Python first."
    exit 1
fi
# Check if the specified Python version is installed
if ! pyenv versions --bare | grep -q "^${PYTHON_VERSION}$"; then
    echo "Python version ${PYTHON_VERSION} is not installed. Falling back to system Python."
    unset PYTHON_VERSION
else
    # Set the local Python version
    pyenv local ${PYTHON_VERSION}
fi

# Create and activate virtual environment if it doesn't exist
if ! pyenv virtualenvs --bare | grep -q "^chartify-env$"; then
    pyenv virtualenv chartify-env
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
else
    echo "Virtual environment 'chartify-env' already exists."
fi
pyenv activate chartify-env

# Install requirements
pip install -r requirements.txt

# Run Flask application
flask run

#deactivate virtual environment when app closes
pyenv deactivate