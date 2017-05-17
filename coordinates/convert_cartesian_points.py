from coordinate_math import *

fp = open("cartesian_points.dat", "r")
points = parse_points(fp) 

outfile = open("polar_points.dat", "w")

for point in points:
    outfile.write(str(cartesian_to_polar(point)) + '\n')

