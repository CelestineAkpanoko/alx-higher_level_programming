#!/bin/bash
# Sends a POST request to a given URL and displays the response
curl -sL -X POSt -d 'email=test%40gmail.com&subject=I+will+always+be+here+for+PLD' "$1"
