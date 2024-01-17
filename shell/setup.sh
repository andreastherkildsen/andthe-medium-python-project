#!/bin/bash

# Move up to working dir
cd ..

# Check if the logs directory already exists
if [ ! -d logs ]; then
    # If not, create the logs directory
    mkdir logs
    echo "Logs directory created."
else
    echo "Logs directory already exists."
fi

# Check if the logs directory already exists
if [ ! -e ".env" ]; then
    # If not, create the logs directory
    cp .env.example .env
    echo ".env file created."
else
    echo ".env file already exists."
fi

