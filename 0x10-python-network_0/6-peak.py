#!/usr/bin/python3
"""finds the peak in a list of unsorted integers"""
def find_peak(list_of_integers):
	"""Find a peak in an unsorted list of integers"""
	if list_of_integers:
		list_of_integers.sort(reverse=True)
		return list_of_integers[0]