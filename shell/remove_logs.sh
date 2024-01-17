#!/bin/bash

# Remove log files from logs directory
find ../logs -type f -name "*.log" -delete

echo "Log files removed from the logs directory."