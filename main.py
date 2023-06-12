import numpy as np
import matplotlib.pyplot as plt

def dilatation_temps(vitesse, altitude, temps_vol, latitude):
    c = 3 * 10**8  # vitesse de la lumière en m/s
    vitesseTerre = 1670 / 3.6 # vitesse de rotation de la Terre en m/s
    G = 6.67430 * 10 ** (-11)  # constante gravitationnelle en m^3 kg^-1 s^-2
    M = 5.972 * 10 ** 24  # masse de la Terre en kg
    R = 6371 * 10 ** 3  # rayon de la Terre en m
    g = G * M / (R + altitude) ** 2 # accélération de la pesanteur en m/s²

    #Calcul du décalage temporel basé sur les formules de Hafele Keating
    delta_t = ((g*altitude) - (vitesseTerre*vitesse*np.cos(latitude*2*np.pi/360)) - (vitesse**2)/2) / (c**2)
    return delta_t * temps_vol * 10**9

#Temps de Hafele Keating
HK_est_xp = -59
HK_ouest_xp = 273
HK_est_prediction = -40
HK_ouest_prediction = 275

# Conditions de vol
temps_vol_est = 41.2 * 3600  # temps de vol vers l'est
temps_vol_ouest = 48 * 3600  # temps de vol vers l'ouest
vitesses_est = np.linspace(0, 500, 50)  # en m/s
vitesses_ouest = np.linspace(-500, 0, 50) # en m/s


# Valeurs fixes d'altitude et de latitude
altitude_est = 8900 # en m
latitude_est = 34 # en degré
vitesse_est = 243 #en m
altitude_ouest = 9360 #en m
latitude_ouest = 31 # en degré
vitesse_ouest = -218 #en m/s


# Calcul de la différence de temps pour chaque paire de vitesse et d'altitude
delta_t_grid_est = dilatation_temps(vitesses_est, altitude_est, temps_vol_est, 34)
delta_t_grid_ouest = dilatation_temps(-vitesses_ouest, altitude_ouest, temps_vol_ouest, 31)

# Valeur de delta_t pour les conditions de vol de Hafele-Keating
simu_HK_est = dilatation_temps(vitesse_est, 8900, temps_vol_est, 34)
simu_HK_ouest = dilatation_temps(vitesse_ouest, 9360, temps_vol_ouest, 31)

# Calcul de delta_t pour les conditions de l'expérience
delta_t_est = dilatation_temps(vitesses_est, altitude_est, temps_vol_est, latitude_est)
delta_t_ouest = dilatation_temps(vitesses_ouest, altitude_ouest, temps_vol_ouest, latitude_ouest)

# Tracé du graphique 2D pour l'est
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# 1er graphie : est
ax1.plot(vitesses_est, delta_t_est)

ax1.scatter([vitesse_est], [simu_HK_est], color='red', label="Valeur calculée dans les conditions de l'expérience")
ax1.scatter([vitesse_est], [HK_est_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
ax1.scatter([vitesse_est], [HK_est_prediction], color='green', label='Valeur théorique de Hafele-Keating')

ax1.set_title('Différence de temps en fonction de la vitesse (Est)')
ax1.set_xlabel('Vitesse (m/s)')
ax1.set_ylabel('Différence de temps (ns)')
ax1.grid(True)
ax1.legend()

# 2ème graphique : ouest
ax2.plot(vitesses_ouest, delta_t_ouest)

ax2.scatter([vitesse_ouest], [simu_HK_ouest], color='red', label="Valeur calculée dans les conditions de l'expérience")
ax2.scatter([vitesse_ouest], [HK_ouest_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
ax2.scatter([vitesse_ouest], [HK_ouest_prediction], color='green', label='Valeur théorique de Hafele-Keating')

ax2.set_title('Différence de temps en fonction de la vitesse (Ouest)')
ax2.set_xlabel('Vitesse (m/s)')
ax2.set_ylabel('Différence de temps (ns)')
ax2.grid(True)
ax2.legend()

plt.tight_layout()
plt.show()









