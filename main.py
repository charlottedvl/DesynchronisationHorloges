import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

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
temps_vol_est = 41.2 * 3600  # en s pour l'est
temps_vol_ouest = 48 * 3600  # en s pour l'ouest
vitesses_est = np.linspace(0, 500, 50)  # en m/s
vitesses_ouest = np.linspace(-500, 0, 50) # en m/s
altitudes = np.linspace(0,15000,50)

# Valeurs fixes d'altitude et de latitude pour Hafele-Keating
altitude_est = 8900 # en m
latitude_est = 34 # en degré
vitesse_est = 243 #en m
altitude_ouest = 9360 #en m
latitude_ouest = 31 # en degré
vitesse_ouest = -218 #en m/s

#Caroll Alley
temps_vol_alley = 30*3600 # en s
altitude_alley = 10500 # en m
vitesse_alley = 500/3.6 # en m/s
latitude_alley = 37 # en degre, qui correspond à Chesapeake Bay dans le Maryland, lieu de l'expérience



# Valeur de delta_t pour les conditions de vol de Hafele-Keating
simu_HK_est = dilatation_temps(vitesse_est, altitude_est, temps_vol_est, 34)
simu_HK_ouest = dilatation_temps(vitesse_ouest, altitude_ouest, temps_vol_ouest, 31)
simu_alley = dilatation_temps(vitesse_alley,altitude_alley,temps_vol_alley, latitude_alley)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))
root = tk.Tk(className='Simulation de Désynchronisation des Horloges Parfaites')
root.title("Simulation de Désynchronisation des Horloges Parfaites")
frame = tk.Frame(root)
frame.pack(side=tk.TOP)

canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=1)




# Fonction appelée lorsque le bouton pour la simulation de Hafele-Keating avec variation d'altitude est cliqué
def plot_hk_altitude():
    delta_t_grid_est = dilatation_temps(vitesse_est, altitudes, temps_vol_est, 34)
    delta_t_grid_ouest = dilatation_temps(vitesse_ouest, altitudes, temps_vol_ouest, 31)
    ax1.clear()
    ax1.plot(vitesses_est, delta_t_grid_est)
    ax1.scatter([vitesse_est], [simu_HK_est], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax1.scatter([vitesse_est], [HK_est_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax1.scatter([vitesse_est], [HK_est_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax1.set_title("Différence de temps en fonction de l'altitude (Est)")
    ax1.set_xlabel('Vitesse (m/s)')
    ax1.set_ylabel('Différence de temps (ns)')
    ax1.grid(True)
    ax1.legend()

    ax2.clear()
    ax2.plot(vitesses_ouest, delta_t_grid_ouest)
    ax2.scatter([vitesse_ouest], [simu_HK_ouest], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax2.scatter([vitesse_ouest], [HK_ouest_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax2.scatter([vitesse_ouest], [HK_ouest_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax2.set_title("Différence de temps en fonction de l'altitude (Ouest)")
    ax2.set_xlabel('Vitesse (m/s)')
    ax2.set_ylabel('Différence de temps (ns)')
    ax2.grid(True)
    ax2.legend()

    if canvas.get_tk_widget() is not None:
        canvas.get_tk_widget().pack_forget()

    canvas.get_tk_widget().pack()
    canvas.draw()

def plot_hk_vitesse():
    delta_t_grid_est = dilatation_temps(vitesses_est, altitude_est, temps_vol_est, 34)
    delta_t_grid_ouest = dilatation_temps(vitesses_ouest, altitude_ouest, temps_vol_ouest, 31)
    ax1.clear()
    ax1.plot(vitesses_est, delta_t_grid_est)
    ax1.scatter([vitesse_est], [simu_HK_est], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax1.scatter([vitesse_est], [HK_est_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax1.scatter([vitesse_est], [HK_est_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax1.set_title('Différence de temps en fonction de la vitesse (Est)')
    ax1.set_xlabel('Vitesse (m/s)')
    ax1.set_ylabel('Différence de temps (ns)')
    ax1.grid(True)
    ax1.legend()

    ax2.clear()
    ax2.plot(vitesses_ouest, delta_t_grid_ouest)
    ax2.scatter([vitesse_ouest], [simu_HK_ouest], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax2.scatter([vitesse_ouest], [HK_ouest_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax2.scatter([vitesse_ouest], [HK_ouest_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax2.set_title('Différence de temps en fonction de la vitesse (Ouest)')
    ax2.set_xlabel('Vitesse (m/s)')
    ax2.set_ylabel('Différence de temps (ns)')
    ax2.grid(True)
    ax2.legend()
    if canvas.get_tk_widget() is not None:
        canvas.get_tk_widget().pack_forget()

    canvas.get_tk_widget().pack()
    canvas.draw()

def plot_HK_altitude():
    delta_t_grid_est = dilatation_temps(vitesse_est, altitudes, temps_vol_est, 34)
    delta_t_grid_ouest = dilatation_temps(vitesse_ouest, altitudes, temps_vol_ouest, 31)
    ax1.clear()
    ax1.plot(altitudes, delta_t_grid_est)
    ax1.scatter([vitesse_est], [simu_HK_est], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax1.scatter([vitesse_est], [HK_est_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax1.scatter([vitesse_est], [HK_est_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax1.set_title("Différence de temps en fonction de l'altitude (Est)")
    ax1.set_xlabel('Vitesse (m/s)')
    ax1.set_ylabel('Différence de temps (ns)')
    ax1.grid(True)
    ax1.legend()

    ax2.clear()
    ax2.plot(altitudes, delta_t_grid_ouest)
    ax2.scatter([vitesse_ouest], [simu_HK_ouest], color='red', label="Valeur calculée dans les conditions de l'expérience")
    ax2.scatter([vitesse_ouest], [HK_ouest_xp], color='blue', label='Valeur expérimentale de Hafele-Keating')
    ax2.scatter([vitesse_ouest], [HK_ouest_prediction], color='green', label='Valeur théorique de Hafele-Keating')
    ax2.set_title("Différence de temps en fonction de l'altitude (Ouest)")
    ax2.set_xlabel('Vitesse (m/s)')
    ax2.set_ylabel('Différence de temps (ns)')
    ax2.grid(True)
    ax2.legend()
    if canvas.get_tk_widget() is not None:
        canvas.get_tk_widget().pack_forget()

    canvas.get_tk_widget().pack()
    canvas.draw()

def plot_alley():
    delta_t_alley_vitesse = dilatation_temps(vitesses_est, altitude_alley, temps_vol_alley, latitude_alley)
    delta_t_alley_altitudes = dilatation_temps(vitesse_alley, altitudes, temps_vol_alley, latitude_alley)
    ax1.clear()
    ax1.plot(vitesses_est, delta_t_alley_vitesse)
    ax1.set_title('Différence de temps en fonction de la vitesse (Alley)')
    ax1.set_xlabel('Vitesse (m/s)')
    ax1.set_ylabel('Différence de temps (ns)')
    ax1.scatter([vitesse_alley], [simu_alley], color='red', label="Valeur calculée dans les conditions de l'expérience")

    ax1.grid(True)

    ax2.clear()

    if canvas.get_tk_widget() is not None:
        canvas.get_tk_widget().pack_forget()

    canvas.get_tk_widget().pack()
    canvas.draw()

button_hk_altitude = tk.Button(frame, text="Hafele-Keating (altitude)", command=plot_hk_altitude)
button_hk_altitude.pack(side=tk.LEFT, padx=10, pady=10)

button_hk_vitesse = tk.Button(frame, text="Hafele-Keating (vitesse)", command=plot_hk_vitesse)
button_hk_vitesse.pack(side=tk.LEFT, padx=10, pady=10)

button_alley = tk.Button(frame, text="Caroll Alley", command=plot_alley)
button_alley.pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()