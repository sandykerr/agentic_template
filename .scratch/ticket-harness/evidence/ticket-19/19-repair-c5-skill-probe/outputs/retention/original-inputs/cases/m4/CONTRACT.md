# CSV records
parse_csv(text) accepts ordinary CSV text using comma delimiters and standard
quoted fields, including an embedded comma and doubled quote escaping. It returns
a fresh tuple of tuple-of-string records, preserving row and field order. No
header handling, external state, persistence or mutation of caller data.
