#!/bin/bash
# Retrieves the status code of a response from a URL
curl -s -o -w "%{http_code}" "$1"
