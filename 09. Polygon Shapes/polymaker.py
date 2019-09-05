import math


#Center Point
x = 257.839
y = 670.593

x = round(x)
x = float(x)
y = round(y)
y = float(y)

verts = \
    [
     (271.254,686.821),
     (276.102,633.332),
     (239.406,633.332),
     (244.290,686.821),
     (257.839,707.804),

     ]


for i in range(len(verts)):
    a = verts[i][0]
    z = verts[i][1]

    a = round(a)
    a = float(a)
    z = round(z)
    z = float(z)

    xvert = a - x
    yvert = z - y
    print int(xvert), int(yvert)





    

