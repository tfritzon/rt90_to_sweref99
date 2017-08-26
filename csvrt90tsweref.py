import pyproj
import sys
import csv

#
# Projections
#

# RT90 2.5 gon V 0:-15
rt90 = pyproj.Proj("+init=EPSG:3021")

# SWEREF99 TM
sweref99 = pyproj.Proj("+init=EPSG:3006")


with open(sys.argv[1]) as fin:
    cfin = csv.reader(fin, delimiter=';')
    cfin.next()
    with open(sys.argv[2], 'w') as fout:
        cfout = csv.writer(fout, delimiter=';')
        cfout.writerow(['NAMN', 'N SWEREF99', 'E SWEREF99'])
        for row in cfin:
            s = row[0]
            x = float(row[1])
            y = float(row[2])
            e,n = pyproj.transform(rt90, sweref99, y, x)
            cfout.writerow([s, int(round(n)), int(round(e))])
