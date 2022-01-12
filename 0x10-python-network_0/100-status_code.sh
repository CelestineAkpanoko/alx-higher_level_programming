#!/bin/bash
# Retrieves the status code of a response from a URL
curl -os /dev/null -w "%{http_code}" "$1"
