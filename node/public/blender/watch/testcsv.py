import csv
import sys

f = open(sys.argv[1], 'rt')
try:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        print row[3]
finally:
    f.close()