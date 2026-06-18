from load_csv import load

print(load("../life_expectancy_years.csv"))
# Error: empty path
print(load(""))
# Error: invalid file format
print(load("../file.txt"))
# File error: [Errno 2] No such file or directory: '../missing.csv'
print(load("../missing.csv"))
# 
print(load("."))
