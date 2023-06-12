import numpy as np
import matplotlib.pyplot as plt

def dilatation_temps(vitesse, altitude, temps_vol):
    # Constantes
    c = 3 * 10**8  # vitesse de la lumière en m/s
    G = 6.67430 * 10**(-11)  # constante gravitationnelle en m^3 kg^-1 s^-2
    M = 5.972 * 10**24  # masse de la Terre en kg
    R = 6371 * 10**3  # rayon de la Terre en m

    # Accélération due à la gravité à l'altitude donnée
    g = G * M / (R + altitude)**2

    # Dilatation du temps due à la vitesse (relativité restreinte)
    delta_t_vitesse = temps_vol / np.sqrt(1 - (vitesse**2 / c**2))

    # Dilatation du temps due à la gravité (relativité générale)
    delta_t_gravite = delta_t_vitesse * (1 + g*altitude / c**2)

    return delta_t_gravite - temps_vol

# Conditions de vol
temps_vol = 40 * 3600  # convertir les heures en secondes
vitesses = np.linspace(200, 300, 100)  # en m/s
altitudes = np.linspace(7000, 12000, 100)  # en m


    # Création d'une grille de vitesses et d'altitudes
vitesse_grid, altitude_grid = np.meshgrid(vitesses, altitudes)

    # Calcul de la différence de temps pour chaque paire de vitesse et d'altitude
delta_t_grid = dilatation_temps(vitesse_grid, altitude_grid, temps_vol)

    # Création du graphique 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

    # Affichage de la surface
surf = ax.plot_surface(vitesse_grid, altitude_grid, delta_t_grid, cmap='viridis')
fig.colorbar(surf)

ax.set_title('Différence de temps en fonction de la vitesse et de l\'altitude')
ax.set_xlabel('Vitesse (m/s)')
ax.set_ylabel('Altitude (m)')
ax.set_zlabel('Différence de temps (s)')

plt.show()













