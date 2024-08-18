#!/bin/bash

echo "BUILD START"

# Install pip if not installed
python3.10 -m ensurepip --upgrade

# Install the dependencies
python3.10 -m pip install --upgrade pip
python3.10 -m pip install -r requirements.txt

# Collect static files
python3.10 manage.py collectstatic --noinput --clear

echo "BUILD END"
