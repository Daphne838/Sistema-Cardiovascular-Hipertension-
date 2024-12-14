import numpy as np
import math as m
import matplotlib.pyplot as plt
import control

x0, t0, tF, dt, w, h = 0, 0, 30, 1E-3, 5, 3
N = round((tF - t0) / dt) + 1
t = np.linspace(t0, tF, N)

u = 2.5 * np.sin(m.pi /2 * t)


# Hipertenso
L, R1, R2, R3, C = 1E-3, 40, 80, 1800, 220E-6

# Definición de la función de transferencia del sistema del caso
num = [R3]
den = [C * L * R2 + C * L * R3, L + C * R1 * R2 + C * R1 * R3, R1 + R2 + R3]
sysHipertenso = control.tf(num, den)
print("Función de transferencia del sistema del caso:", sysHipertenso)



# Normotenso
L, R1, R2, R3, C = 1E-3, 150, 300, 1500, 220E-6

# Definición de la función de transferencia del sistema del control
num = [R3]
den = [C * L * R2 + C * L * R3, L + C * R1 * R2 + C * R1 * R3, R1 + R2 + R3]
sysNormotenso = control.tf(num, den)
print("Función de transferencia del sistema del caso:", sysNormotenso)



# Controlador PID
Rr, Re, Cr, Ce = 35035, 103.31, 2.5E-6, 1.12E-5

# Definición de la función de transferencia del PID
numPID = [Rr * Re * Cr * Ce, Re * Ce + Rr * Cr, 1]
denPID = [Re * Cr, 0]

PID = control.tf(numPID, denPID)
print("Función de transferencia del PID:", PID)

# Configuración del sistema en lazo cerrado con el controlador PID
X = control.series(PID, sysHipertenso)
sysPID = control.feedback(X, 1, sign=-1)
print("Sistema en lazo cerrado con PID:", sysPID)



# =============================================================================
# RESPIRACIÓN NORMAL
# =============================================================================
# Gráfico para el caso de respiración normal
fig1 = plt.figure()
ts, controlNormotenso = control.forced_response(sysNormotenso, t, u, x0)
ts, controlHipertenso = control.forced_response(sysHipertenso, ts, u, x0)
plt.plot(t, controlNormotenso, '-', color='g', label='Normotenso')
plt.plot(t, controlHipertenso, '-', color='r', label='Hipertenso')
ts, controlHipertenso = control.forced_response(sysHipertenso, ts, controlNormotenso, x0)
ts, controlPID = control.forced_response(sysPID, ts, controlHipertenso, x0)
plt.plot(t, controlPID, '--', color='b', label='Tratamiento')

plt.grid(False)  # Quita la cuadrícula del fondo
plt.xlim(0, 30)
plt.ylim(-3,3)
plt.xticks(np.arange(0,31,5))
plt.xlabel('t [segundos]', fontsize=11)
plt.ylabel('V(t) [volts]', fontsize=11)
plt.yticks(np.arange(-3,3.5,0.5))
plt.legend(bbox_to_anchor=(0.5,-0.28),loc='center',ncol=4)
plt.show()
fig1.set_size_inches(w, h)
fig1.tight_layout()
fig1.savefig('SPYDER.png', dpi=600)
fig1.savefig('SPYDER.pdf')
