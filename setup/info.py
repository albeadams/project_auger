

list_missing_values_options = """\n  
  Your data has missing values.
  Here are your options on how to handle this:\n
      1. Remove offending row
      2. Remove offending column
      3. Replace with zero
      4. Replace with min
      5. Replace with max
      6. Replace with average
      7. Replace with median
      8. Replace with most frequent
      9. Forward fill
      10. Backward fill
      11. Forward fill then backward fill
      12. Linear interpolation
      13. Index interpolation (use index values)
        (scipy interpoloation to come...)
      \n"""


no_missing_found = """\n
  No missing data was found in the training set. Any missing data found
  in the test set, or any future data, will be set to zero.\n"""