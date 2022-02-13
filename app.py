from shapely.geometry import Point, Polygon
# import matplotlib.pyplot as plt

# script to convert standard coords (i.e. 32°26'37.31"N) to decimal format
def conversion(old):
    # Create object to translate letters to decimal values
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}

    # swap out odd characters
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')

    # split string into list so that it's pieces can be accessed individually
    new = new.split()

    # getting the direction from NWSE, determines if end value will be positive or negative
    new_dir = new.pop()
    new.extend([0,0,0])

    # math to convert coords as [hours, minutes, seconds] to decimal value
    return (float(new[0])+float(new[1])/60.0+float(new[2])/3600.0) * direction[new_dir]


# accepts list of neighborhood coordinates, and a home coordinate 
# to see if the coordinate would be contained within the neighborhood
def ftth_checker(neighborhood, home):
    # initialize list to store decimal coordinates
    decimal_coords = []

    home_coords = Point(conversion(home['lattitude']), conversion(home['longitude']))
    # loop through neighborhood coordinate list, convert each set to decimals, add to list as a tuple
    for coord in neighborhood:
        decimal_coords.append((conversion(coord['lattitude']), conversion(coord['longitude'])))
    
    # convert coordinates to digital polygon (memory only)
    poly = Polygon(decimal_coords)

    # uncomment below lines to show a visual representation of the coordinates
    # note, the conversion from spherical data (gps) to flat data (display) is super low-powered,
    # helpful for troubleshooting only. You'll also need to uncomment the import matplotlib at the top of the file
    

    """Init display window"""
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True

    """Plot shape"""
    # x, y = poly.exterior.xy
    # plt.plot(x, y, c="red")

    """Plot Point"""
    # plt.scatter([home_coords.x], [home_coords.y], c="blue")

    """Show Plot"""
    # plt.show()

    return home_coords.within(poly)


    