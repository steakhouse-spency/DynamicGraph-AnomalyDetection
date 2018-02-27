#!/bin/bash

# Run first time you install
############################

# Update virtualenv
sudo pip install --upgrade virtualenv

# Create virtual environment
virtualenv -p python3 pythonenv

# Activate virtual environment
source pythonenv/bin/activate

# Install requirments
sudo pip install -r requirements.txt
