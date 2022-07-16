a=input()
h=(ord(a[0])-48)*10+ord(a[1])-48
m=(ord(a[3])-48)*10+ord(a[4])-48
if m%2==0:
    an=30*h*1.0-11*m/2
    if an<0:
        an+=360
    if an>180:
        an=360-an
    print("{:.1f}".format(an))
else:
    an=30*h*1.0-5.5*m
    if an<0:
        an+=360
    if an>180:
        an=360-an
    print("{:.1f}".format(an))