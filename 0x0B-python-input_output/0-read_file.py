#!/usr/bin/python3
# file: 0-read_file.py
""" Describes a text file-reading function."""

def read_file(filename=""):
    """ This function reads and prints text in a file."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
