from shapely.geometry import Point, Polygon

# Create Point objects, customer home coordinates
p1 = Point(24.952242, 60.1696017)
p2 = Point(24.976567, 60.1612500)

# Create a Polygon
coords = [(24.950899, 60.169158), (24.953492, 60.169158), (24.953510, 60.170104), (24.950958, 60.169990)]
poly = Polygon(coords)

print(p1)
print(p2)
print(coords)
print(poly)

print("Is p1 inside the polygon? ", p1.within(poly))
print("Is p2 inside polygon? ", p2.within(poly))

# script to convert standard coords (i.e. 32°26'37.31"N) to decimal format
def conversion(old):
    # object to generate int factor for cardinal directions
    direction = {'N':1, 'S':-1, 'E': 1, 'W':-1}
    
    # filter out weird symbols
    new = old.replace(u'°',' ').replace('\'',' ').replace('"',' ')

    #break up the hours, minutes, and seconds
    new = new.split()
    new_dir = new.pop()
    new.extend([0,0,0])
    return (int(new[0])+int(new[1])/60.0+int(new[2])/3600.0) * direction[new_dir]


def ftth_checker(neighborhood, home):
    print(neighborhood)