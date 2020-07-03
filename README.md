# CSVScreen
# Language: Python
# Input: TXT (keyword-value pairs)
# Output: CSV (indexed)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: numpy==1.16.0

A PluMA plugin that takes a CSV file and removes all rows with
a user-specified column set to zero or non-zero, creating a new CSV file with the remaining columns.

The plugin takes as input a tab-separated file of three keyword value
pairs: csvfile (name of the input CSV file), column (the name of the column
to remove, which should also appear in the header or first row of the CSV file).
and criteria (zero or non-zero)

This can be useful when viewing for example the effects of another variable
when removing a specific target..

