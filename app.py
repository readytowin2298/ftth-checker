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



def ftth_checker(neighborhood, home):
    print(neighborhood)