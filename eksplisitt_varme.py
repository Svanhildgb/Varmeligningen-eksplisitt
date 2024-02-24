import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

#Matematiske verdier 
L = 1 #Lengde på stang
T = 0.15 #Total tid som simuleres

#Antall punkter i rom og tid
N_x = 50
N_t = 2000

h = L/(N_x-1) #steg i x-retning
k = T/(N_t-1) #steg i t-retning

#Alpha
a = k/(h**2)

# Sjekker stabilitetskriteriet til aplha,
if a >= 0.5:
    raise ValueError('Stabilitetskriteriet til k/h^2 er ikke oppfylt!')
else:
    print("Alpha er:", a, ", alt er good og vi kjører på.")


#Gitterpunktene
x = np.linspace(0, L, N_x)
t = np.linspace(0, T, N_t)

#2D matrisen som har dimensjoner N_x og N_t
u = np.zeros((N_x,N_t))

#Startfunksjonen/initialbetingelsen
def funk(x):
    #retun x
    #return x**2
    #return (1/np.sqrt(2*np.pi))*np.exp(-(x**2)/(2))
    return np.sin(np.pi*x)

# Initialbetingelse
u[1:-1, 0] = funk(x[1:-1])
# 1:-1 tar med alle elementene fra indeks 1 frem til nest siste indeks fordi disse to er randen. ,0 gir oss det første elementet langs t-aksen


# Oppdateringsfunksjon
def oppdater_u():
    for j in range(0, N_t - 1):
        u[1:-1, j + 1] = a * u[0:-2, j] + (1 - 2 * a) * u[1:-1, j] + a * u[2:, j]

# Kjør oppdateringsfunksjonen
oppdater_u()

#Plott
fig, axs = plt.subplots(subplot_kw={"projection": "3d"})
meshX, meshT = np.meshgrid(x, t)
axs.plot_surface(meshX, meshT, np.flip(np.rot90(u), axis=0), cmap=cm.hsv)

axs.set_xlabel("pos")
axs.set_ylabel("tid")
axs.set_zlabel("temp")

plt.show()