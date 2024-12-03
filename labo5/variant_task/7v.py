import matplotlib.pyplot as plt
import math

ymin=None
xcos=None
cas=[]
x=[]
y=[]
xv = -1
while xv <= 2:
    per=0
    if xv <= 1:
        yv = math.exp(-2 * math.sin(xv))
        if ymin==None:
            ymin=yv
            per=1
        if ymin>yv:
            ymin=yv
            per=1
    else:
        yv = xv**2 - math.cos(xv) / math.sin(xv)
        if ymin>yv:
            ymin=yv
            per=1
    x.append(xv)
    y.append(yv)
    if per==1:
        xcos=xv
    xv += 0.1
    
xv=-1
while xv <= 2:
    cas.append(ymin)   
    xv += 0.1
plt.scatter(xcos, ymin, color='green')
plt.annotate('Точка касания', xy=(xcos, ymin))
plt.plot(x, y)
plt.plot(x,cas,label='касательная')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции 7 вариант')
plt.legend()
plt.show()
