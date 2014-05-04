#!/bin/bash

# Create a virtualenv named flask-env
VIRTUALENV=`which virtualenv`
VIRTUALENV_NAME="flask-env"
DOWNLOADS="$VIRTUALENV_NAME/downloads"

mkdir -p $DOWNLOADS
$VIRTUALENV --no-site-packages --distribute $VIRTUALENV_NAME &&
    source $VIRTUALENV_NAME/bin/activate &&
    pip install --allow-all-external --download $DOWNLOADS -r requirements.txt

# pip install --no-index --find-links=$DOWNLOADS -r requirements.txt
