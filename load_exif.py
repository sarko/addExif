'''

load_exif.py

Parameters:
    infiles: list of filename (can be absolutely or relatively pathed) provided on the command line

    camera positions:  expects a file called 'CameraPositions.txt' that is comma delimited.  First line
    of file is input projection (ala EPSG:32606) and remaining lines are of the form
    imageFilename,easting,northing,height


Requires:
    pyproj needs to be installed for projection transformations
    exif.py (from https://gist.github.com/c060604/8a51f8999be12fc2be498e9ca56adc72)
        - exif.py is also included in this repo since it must be present for load_exif.py, however, I 
        claim no ownership of it nor do I guarantee the result


Usage:
    python load_exif.py <image1.jpg> <image2.jpg> ... <imageN.jpg> 

    or 

    python load_exif.py *.jpg



'''




import sys, re
from exif import set_gps_location
from pyproj import Proj, transform

infiles = sys.argv[1:]

loc_file = 'CameraPositions.txt'
loc_data = open(loc_file,'r').readlines()

# First line of position file is expected to define the input 
# projection by EPSG code
inProj = loc_data[0].rstrip()
pin = Proj(init=inProj)
pout = Proj(init='EPSG:4326')


for fi in infiles:
    # split file name just in case it is pathed, fname will contain just the filename
    # which is what is expected in the position file
    fname = re.split('/',fi)[-1]

    for line in loc_data[1:]:
        # Format of camera position file is fname, easting, northing, alt
        t = re.split(',',line)

        if t[0] == fname:
            east = float(t[1])
            north = float(t[2])
            alt = float(t[3])

            lon,lat = transform(pin,pout,east,north)

            set_gps_location(fi,lat,lon,alt)









