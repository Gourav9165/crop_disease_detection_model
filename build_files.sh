#!/bin/bash

echo "BUILD START"

# Install pip if not installed
python3.9 -m ensurepip --upgrade

# Install the dependencies
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
