import numpy as np

# Parâmetros do ruído
a1 = 0.5  
a2 = 0.3  
f1 = 5500 
f2 = 5800
fs = 13000 
duration = 5  

# Vetor de tempo
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Gerar o ruído r(t)
r_t = a1 * np.cos(2 * np.pi * f1 * t) + a2 * np.cos(2 * np.pi * f2 * t)

# Exportar ruído para análise (opcional)
from scipy.io.wavfile import write
write("ruido.wav", fs, np.int16(r_t / np.max(np.abs(r_t)) * 32767))
