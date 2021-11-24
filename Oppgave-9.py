# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 09:47:22 2021

@author: sverr
"""
# =============================================================================
# TMM4115 Produktmodellering  MTP, NTNU 
#    Side 6 av 8 
#  
# Oppgave 9. Beregning av største innskrevne sirkel og rundhet (Python-
# oppgave) 
#   
# På delen som er vist over er det tatt 8 målepunkter i hullet. Målepunktene er
# lagt inn i et Python-
# script: 
# import numpy 
# #Målepunkter i x-y-planet 
# punkterXY = numpy.array([[30.082, 0.078], 
#                          [21.276, 21.307], 
#                          [0.071, 30.096], 
#                          [-21.147, 21.298], 
#                          [-29.921, 0.083], 
#                          [-21.121, -21.148], 
#                          [0.079, -29.916], 
#                          [21.440, -21.131]]) 
#  
#  
# a)  Lag et program som har en funksjon (def...) som beregner avstanden fra et
# målepunkt og til 
# sirkelsenteret x = 0 og y = 0 
# b)  Lag et program som beregner diameteren til største innskrevne sirkel i 
#hullet. Bruk gjerne 
# programmet fra a) som utgangspunkt. Hva er x- og y-koordinatene til 
#sirkelsenteret for denne 
# sirkelen? 
# c) Beregn rundheten av hullet. Hva er x- og y-koordinatene til sirkelsenteret 
#som ligger til grunn for 
# denne beregning av rundhet? 
#  
# Leveranse: Svar på deloppgave, inkl. Python-kode.
# =============================================================================


import numpy as np
import matplotlib.pyplot as plt

#Oppgave 9a
punkterXY = np.array([[30.082, 0.078], 
                        [21.276, 21.307], 
                        [0.071, 30.096], 
                        [-21.147, 21.298], 
                        [-29.921, 0.083], 
                        [-21.121, -21.148], 
                        [0.079, -29.916], 
                        [21.440, -21.131]])



# a)  Lag et program som har en funksjon (def...) som beregner avstanden fra 
#et målepunkt og til sirkelsenteret x = 0 og y = 0 

def avstand_til_sirkelsenter(p1, senter):
  return np.sqrt((p1[0]-senter[0])**2+(p1[1]-senter[1])**2) # Pythagorean theorem


#Finner avstand for hvert punkt i senter x=0, y=0
def avstander_radius(liste_med_punkter, senter):
    avstand = {}
    for i in range(len(liste_med_punkter)):
        avstand[i] = format(avstand_til_sirkelsenter((liste_med_punkter[i][0], 
                                                      liste_med_punkter[i][1]), 
                                                     senter), '.4f')
        
    #Sorterer avstandene fra kortest avstand til lengst    
    sort_orders = sorted(avstand.items(), key=lambda x: x[1], reverse=False)


    list(sort_orders)
    
    return sort_orders

    
print('Avstander til origo fra kortest til lengst: ')    
avstander_til_origo = avstander_radius(punkterXY, (0, 0))
    #Printer alle avstandene
for i in avstander_radius(punkterXY, (0, 0)):
    print(i[0], i[1])
print('')

#Oppgave 9b
# b)  Lag et program som beregner diameteren til største innskrevne sirkel i hullet. Bruk gjerne 
# programmet fra a) som utgangspunkt. Hva er x- og y-koordinatene til sirkelsenteret for denne 
# sirkelen?

#Tar inn en liste med punkter og returnerer diametere til største innskrevne sirkel samt senter
def diameter_innskreven_sirkel(liste_med_punkter):
    senter_array_x = np.arange(-0.12, 0.12, 0.01)
    senter_array_y = np.arange(-0.12, 0.12, 0.01)
    
    (max_x, max_y) = (0, 0)
    max_radius = 0
    f = open('alle_punkter.txt', 'w')
    for x_verdi in senter_array_x:
        for y_verdi in senter_array_y:
            (x_verdi1, y_verdi1) = (format(x_verdi, '.2f'), format(y_verdi, '.2f'))
            f.write(f'{x_verdi1}, {y_verdi1}\n')
            liste_med_radiuser = avstander_radius(liste_med_punkter, (x_verdi, y_verdi))
            if float(liste_med_radiuser[0][1]) > float(max_radius):
                max_radius = float(liste_med_radiuser[0][1])
                
                (max_x, max_y) = (x_verdi, y_verdi)
    f.close()
    max_diameter = 2 * max_radius
    
    return max_diameter, (max_x, max_y)        

#Svarer på spørsmål i oppgave b:
(x_b, y_b) = diameter_innskreven_sirkel((punkterXY))[1][0], diameter_innskreven_sirkel(punkterXY)[1][1]
d_b = float(diameter_innskreven_sirkel((punkterXY))[0])
print('Diameteren til største innskrevne sirkel i hullet:', format(d_b, '.3f'))
print('X- og y-koordinatene til sirkelsenteret: x =', format(x_b, '.6f'), ' y = ', format(y_b, '.6f'))

print()

# c) Beregn rundheten av hullet. Hva er x- og y-koordinatene til sirkelsenteret som ligger til grunn for 
# denne beregning av rundhet?

def finn_rundhet(liste_med_punkter):
    senter_array_x = np.arange(-0.12, 0.12, 0.01)
    senter_array_y = np.arange(-0.12, 0.12, 0.01)
    
    (max_x, max_y) = (0, 0)
    rundhet = 100
    rundhet_min = 99
    g = open('rundhet_med_punkter.txt', 'w')
    for x_verdi in senter_array_x:
        for y_verdi in senter_array_y:
            
            liste_med_radiuser = avstander_radius(liste_med_punkter, (x_verdi, y_verdi))
            (x_verdi1, y_verdi1) = (format(x_verdi, '.2f'), format(y_verdi, '.2f'))

            rundhet = float(liste_med_radiuser[7][1])-float(liste_med_radiuser[0][1])
            rundhet1 = format(rundhet, '.4f')
            
            g.write(f'{rundhet1} ; ({x_verdi1}, {y_verdi1})\n')
            
            if rundhet < rundhet_min:
                rundhet_min = rundhet
                (max_x, max_y) = (x_verdi, y_verdi)
    g.close()
    
    return rundhet_min, (max_x, max_y)

(x_c, y_c) = (finn_rundhet(punkterXY)[1][0], finn_rundhet(punkterXY)[1][1])
rundhet_c = float(finn_rundhet(punkterXY)[0])

print('Rundheten til hullet er:', format(rundhet_c, '.3f'))
print('X- og y-koordinatene til sirkelsenteret som ligger til grunn for denne beregning av rundhet: x =', format(x_c, '.3f'), ' y = ', format(y_c, '.3f') )

'''
Plotting
'''
#a
for i in range(len(punkterXY)):
    plt.plot(punkterXY[i][0],punkterXY[i][1] , 'or', 20.0)
plt.plot(0,0 , 'or', markersize=2)

#b
def tegne_sirkel(senter, radius):
    y_pluss = []
    for x in range(-30, 31, 1):
        #print('lol', np.sqrt(((radius**2)-((x-senter[0])**2))))
        y_pluss.append(senter[1] + np.sqrt(abs((radius**2)-((x-senter[0])**2))))
    y_minus = []
    for x in range(-30, 31, 1):
        #print('lol', np.sqrt(((radius**2)-((x-senter[0])**2))))
        y_minus.append(senter[1] - np.sqrt(abs((radius**2)-((x-senter[0])**2))))
    return y_pluss, y_minus

x_sirkel = np.arange(-30, 31, 1)
plt.plot(diameter_innskreven_sirkel(punkterXY)[1][0], diameter_innskreven_sirkel(punkterXY)[1][1], 'ob', markersize=2)
plt.plot(x_sirkel, tegne_sirkel((x_b, y_b), (d_b)/2)[0], 'b', linewidth=0.5)
plt.plot(x_sirkel, tegne_sirkel((x_b, y_b), (d_b)/2)[1], 'b', linewidth=0.5)

#c
plt.legend(['Punkter', 'Største innskrevne sirkel'], loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2)
plt.show()
