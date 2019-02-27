# addExif

load_exif.py

Parameters:<br>
    infiles: list of filename (can be absolutely or relatively pathed) provided on the command line
    <br>
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



