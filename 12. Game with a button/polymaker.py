import math


#Center Point
x = 283.490
y = 201.363

x = round(x)
x = float(x)
y = round(y)
y = float(y)

verts = \
    [
     (316.258,193.917),
     (313.250,186.423),
     (316.084,178.838),

     (323.790,175.637),
     (331.284,178.891),
     (334.500,186.423),

     (331.375,194.129),

     (323.790,197.262),
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





    

