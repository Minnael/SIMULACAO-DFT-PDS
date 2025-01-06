import numpy as np

# Parâmetros do ruído
a1 = 0.5  # Amplitude da primeira senóide
a2 = 0.3  # Amplitude da segunda senóide
f1 = 5500  # Frequência da primeira senóide (Hz)
f2 = 5800 # Frequência da segunda senóide (Hz)
fs = 13000 # Taxa de amostragem (Hz)
duration = 5  # Duração do sinal (segundos)

# Vetor de tempo
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

# Gerar o ruído r(t)
r_t = a1 * np.cos(2 * np.pi * f1 * t) + a2 * np.cos(2 * np.pi * f2 * t)

# Exportar ruído para análise (opcional)
from scipy.io.wavfile import write
write("ruido.wav", fs, np.int16(r_t / np.max(np.abs(r_t)) * 32767))
