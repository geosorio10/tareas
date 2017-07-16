import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

n_puntos=300

x=np.linspace(0.0,30.0,n_puntos)
y=np.linspace(0.0,30.0,n_puntos)


matriz=np.zeros((n_puntos,n_puntos))

matriz[30,150]=-0.5


u_inicial=matriz #forma inicial de la onda

c=1.0
delta_x=x[1]-x[0]
delta_y=y[1]-y[0]
delta_t=0.0005 #con esto se cumple que gamma y beta sean menores de 1

gamma=(c* delta_t)/delta_x
beta=(c*delta_t)/delta_y

#condiciones de frontera fijas

rejilla_posicion= int((2*n_puntos)/3)

u_inicial[0]=0.0
u_inicial[n_puntos-1]=0.0
u_inicial[:,0]=0.0
u_inicial[:,n_puntos-1]=0.0

for i  in range(0,n_puntos):
    if(i<=140):
        u_inicial[rejilla_posicion,i]=0.0
    if(i>=161):
        u_inicial[rejilla_posicion,i]=0.0

u_siguiente=np.zeros((n_puntos,n_puntos))

u_siguiente[0]=0.0
u_siguiente[n_puntos-1]=0.0
u_siguiente[:,0]=0.0
u_siguiente[:,n_puntos-1]=0.0

for i  in range(0,n_puntos):
    if(i<=140):
        u_siguiente[rejilla_posicion,i]=0.0
    if(i>=161):
        u_siguiente[rejilla_posicion,i]=0.0



for j in range(1,n_puntos-1):
    for i in range(1,n_puntos-1):
        u_siguiente[j,i]=0.5*( (gamma**2)*(u_inicial[j,i+1]-2.0*u_inicial[j,i]+u_inicial[j,i-1])+(beta**2)*(u_inicial[j+1,i]-2.0*u_inicial[j,i]+u_inicial[j-1,i])+2.0*u_inicial[j,i] )

u_pasado=u_inicial.copy()
u_presente=u_siguiente.copy()

n_tiempo=60
for l in range(n_tiempo):
    for i in range(1,n_puntos-1):
        for j in range(1,n_puntos-1):
            u_siguiente[j,i]=(gamma**2)*(u_presente[j,i+1]-2.0*u_presente[j,i]+u_presente[j,i-1])+(beta**2)*(u_presente[j+1,i]-2.0*u_presente[j,i]+u_presente[j-1,i])+2.0*u_presente[j,i]-u_pasado[j,i]
        u_pasado=u_presente.copy()
        u_presente=u_siguiente.copy()







#grafica

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

xGrid, yGrid=np.meshgrid(y,x)

#ax.plot_wireframe(xGrid, yGrid, u_presente, rstride=1, cstride=1)


