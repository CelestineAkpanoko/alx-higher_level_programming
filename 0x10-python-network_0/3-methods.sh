#!/bin/bash
# Display all server allowable HTTP methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
