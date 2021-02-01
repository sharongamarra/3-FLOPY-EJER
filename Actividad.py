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
#IMS solucion del modelo interativo
ims = flopy.mf6.ModflowIms(sim, pname="ims", complexity="SIMPLE")

#Crear un modelo de flujo subterranea
model_nam_file = "{}.nam".format(name)
gwf = flopy.mf6.ModflowGwf(sim, modelname=name, model_nam_file=model_nam_file)

#Definir discretización del modelo
bot = np.linspace(-H / Nlay, -H, Nlay)
delrow = delcol = L / (N - 1)
dis = flopy.mf6.ModflowGwfdis(
    gwf,
    nlay=Nlay,
    nrow=N,
    ncol=N,
    delr=delrow,
    delc=delcol,
    top=0.0,
    botm=bot,
)

#Crear paquete de condiciones iniciales
start = h1 * np.ones((Nlay, N, N))
ic = flopy.mf6.ModflowGwfic(gwf, pname="ic", strt=start)

#Crear paquete NPF Flujo de propiedad de nodo
npf = flopy.mf6.ModflowGwfnpf(gwf, icelltype=1, k=k, save_flows=True)
