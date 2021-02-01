#Importar
import os
import numpy as np
import matplotlib.pyplot as plt
import flopy

#parametros del modelo
name = "tutorial01_mf6"
h1 = 100
h2 = 90
Nlay = 10
N = 101
L = 400.0
H = 50.0
k = 1.0

#Creando simulación de flopy
sim = flopy.mf6.MFSimulation(
    sim_name=name, exe_name=C:/12-DIPLOMADO/Programas/mf6.2.0/bin/mf6, version="mf6", sim_ws="."
)

#TDIS Paquete de discretización temporal
tdis = flopy.mf6.ModflowTdis(
    sim, pname="tdis", time_units="DAYS", nper=1, perioddata=[(1.0, 1, 1.0)]
)