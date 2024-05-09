#### This code has been designed and written by Horacio Irán Solís-Cisneros
##### Lecturer in Software Engineering at Universidad Politécnica de Chiapas
##### PhD. Student in Tecnológico Nacional de México campus Tuxtla Gutiérrez

import numpy as np
import os
import matplotlib.pyplot as plt

# Constants
E_g_InN = 0.7   
E_g_GaN = 3.4
E_p_InN = 0.8   
E_p_GaN = 3.4
b_Eg = 1.43
b_Ep = 1.00
#Dumping coefficient for Aspnes model
#https://doi.org/10.1134/S1063782607090102
gamma = 0.08     
# In molar fraction range
x = np.arange(0, 1, 0.01)
# Wavelengths
wavelengths = np.arange(100, 2000, 10)
energies = 1240/wavelengths
# Create folder for results
folder = 'refractive_index'
file_ext = '.nk'
if not os.path.exists(folder):
    os.makedirs(folder)
# Calculate and save the refractive index for each x
for i in range(len(x)):
    # Calculate energy from Vegard's law without bowing factor
    E_g = x[i]*E_g_InN + (1-x[i])*E_g_GaN -b_Eg*x[i]*(1-x[i])
    E_p = x[i]*E_p_InN + (1-x[i])*E_p_GaN-b_Ep*x[i]*(1-x[i])
    # Calculate refractive index
    n = np.sqrt(1 + (E_p**2 * energies**2)/(energies**2 - E_g**2) - gamma*1j)
    # Save file in CSV format
    filename = folder + '/x_' + str(x[i]) + file_ext
    #header = 'wavelength,n_real,n_imaginary'
    ##np.savetxt(filename, np.column_stack((wavelengths, n.real, n.imag)), 
    ##           fmt='%.3f', delimiter=',', header=header)
    np.savetxt(filename, np.column_stack((wavelengths, n.real, n.imag)), 
               fmt='%.3f', delimiter=' ')
# Graficar  
for i in range(len(x)):
    filename = folder + '/x_' + str(x[i]) + file_ext
    data = np.genfromtxt(filename, delimiter=' ', skip_header=1)
    plt.plot(data[:,0], data[:,1], '-', label='x='+str(x[i]))
    plt.plot(data[:,0], data[:,2], '--', linewidth=1.5)
#plt.legend()
plt.xlabel('Wavelength (nm)')
plt.ylabel('Refractive Index')
plt.show()
