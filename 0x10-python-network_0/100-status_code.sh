#!/bin/bash
# Retrieves the status code of a response from a URL
curl -s -w "%{status_code}" -o /dev/null "$1"
