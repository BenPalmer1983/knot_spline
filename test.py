import numpy
from knot_spline import knot_spline
import matplotlib.pyplot as plt


print("Fixed End")

pf = numpy.zeros((10,),)
p = numpy.zeros((7,),)
x = numpy.linspace(0.0,7.0,1001)


pf[0] = 0.0
pf[1] = 1.0
pf[2] = 2.0
pf[3] = 3.0
pf[4] = 4.0
pf[5] = 5.0
pf[6] = 6.0
pf[7] = 7.0    # fixed end x
pf[8] = 7.0    # fixed end v(x)
pf[9] = 10.0   # fixed end v'(x)

p[0] = 0.0
p[1] = 1.0
p[2] = 2.0
p[3] = 1.0
p[4] = 4.0
p[5] = 3.0
p[6] = 6.0



y = knot_spline.cubic_knot_spline_fixed_end_v(x, p, pf)


plt.plot(x,y)
plt.show()




print("Points")

pf = numpy.zeros((8,),)
p = numpy.zeros((8,),)
x = numpy.linspace(0.0,7.0,1001)


pf[0] = 0.0
pf[1] = 1.0
pf[2] = 2.0
pf[3] = 3.0
pf[4] = 4.0
pf[5] = 5.0
pf[6] = 6.0
pf[7] = 7.0

p[0] = 0.0
p[1] = 1.0
p[2] = 2.0
p[3] = 4.0
p[4] = 2.0
p[5] = 1.0
p[6] = 0.5
p[7] = 0.0



y = knot_spline.cubic_knot_spline_v(x, p, pf)


plt.plot(x,y)
plt.show()











