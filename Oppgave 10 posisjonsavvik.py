# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 13:00:01 2021

@author: Marius
"""
import numpy as np

#Målinger

Punkter_senterlinje = np.array([[40.058, 30.042, 25.112],
                               [40.029, 30.027, 20.013],
                               [40.023, 30.032, 14.879],
                               [39.998, 29.991, 3.910]])

Punkter_toppflate = np.array([[9.965, 9.997, 29.993],
                             [10.013, 49.991, 29.997],
                             [29.957, 9.994, 30.021],
                             [30.037, 50.001, 29.988],
                             [50.003, 10.003, 29.986],
                             [49.957, 49.998, 29.984],
                             [69.997, 9.992, 30.037],
                             [70.035, 49.996, 30.039],
                             [89.964, 10.002, 29.998],
                             [89.994, 49.999, 30.058]])
"""
Oppgave a) Det er spesifisert en toleranse på rettvinklethet for senterlinjen 
til hullet. Beregn avviket i rettvinklethet ut fra målingene som er vist i
Tabell 1. Er avviket innenfor toleransen?
"""


def rettvinkelhet(punkter, x_referanse, y_referanse):
    avvik = []#lager tom liste
    for i in range(len(punkter)):
        x_avvik = x_referanse - punkter[i][0]
        y_avvik = y_referanse - punkter[i][1]
        avvik.append(np.sqrt(x_avvik**2 + y_avvik**2))
    avvik.sort()
    feil = abs(avvik[0]-avvik[-1])
    return feil

print("Rettvinkelavvik",rettvinkelhet(Punkter_senterlinje, 40, 30),"mm")

def rettvinkelhet2(punkter):
    avvik = []#lager tom liste
    for i in range(len(punkter)):
        x_avvik = punkter[i][0]
        for j in range(len(punkter)):
            y_avvik = punkter[i][1]
            avvik.append(x_avvik-y_avvik)
    avvik.sort()
    feil = abs(avvik[0]-avvik[-1])
    return feil

print("Rettvinkelavvik2",rettvinkelhet2(Punkter_senterlinje),"mm")

"""
b)  Det er spesifisert en toleranse på posisjonen av senterlinjen til hullet.
    Beregn avviket i posisjon ut fra målingene som er vist i Tabell 1.
    Er avviket innenfor toleransen?
"""

def posisjonsavvik(punkter, x_referanse, y_referanse):
    avvik = []
    for i in range(len(punkter)):
        x_avvik = x_referanse - punkter[i][0]
        y_avvik = y_referanse - punkter[i][1]
        avvik.append(np.sqrt(x_avvik**2 + y_avvik**2))
    avvik.sort()
    feil = avvik[-1]
    return feil

print("Posisjonsavvik:",posisjonsavvik(Punkter_senterlinje, 40, 30),"mm")



"""
C)
"""
def pararellitet(punkter):
    z_punkter = []
    for i in range(len(punkter)):
        z_punkter.append(punkter[i][2]) 
    z_punkter.sort()
    avvik = z_punkter[-1]-z_punkter[0]
    return avvik

print("Pararellitet:", pararellitet(Punkter_toppflate), "mm")

"""
D)
"""

def flateform(punkter, referanse):
    z_punkter = []
    for i in range(len(punkter)):
        z_punkter.append(abs(referanse-punkter[i][2]))
    z_punkter.sort()
    return 2*z_punkter[-1]


print("Flateform:", flateform(Punkter_toppflate, 30),"mm")

