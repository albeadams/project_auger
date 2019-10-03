

missingvalues = """\n  
  Your data has missing values.
  Here are your options on how to handle this:\n
      1. Remove offending row
      2. Remove offending column
      3. Replace missing values with... (to come) [min, max, avg,ffill, bfill]\n"""


replacewithoptions = """\n
  You chose to replace the missing values. There are several options:

    1. Replace with min
    2. Replace with max
    3. Replace with average
    4. Forward fill
    5. Backward fill
    6. Interpolate???

    [HERE - https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
      also note hands on... need to store whatever this is for use in test and later data...
      need to go back and split the data into test and train data before this, obtain 
      this fill value only from test]

      \n"""

nomissingfound = """\n
  No missing data was found in the training set. Any missing data found
  in the test set, or any future data, will be set to zero.
      \n"""