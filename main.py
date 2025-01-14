from functions_convolve import *
from functions_graph import *
from function_noise import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
from scipy.io.wavfile import write, read

# ===============================================================
# PASSO 1: SIMULAÇÃO INICIAL COM SINAIS ALEATÓRIOS
# ===============================================================

# PARÂMETROS
N = 1024  # NÚMERO DE PONTOS DA FFT
M = 150  # TAMANHO DO FILTRO
L = N - M + 1

# GERARANDO SINAIS ALEATÓRIOS
np.random.seed(42)
x = np.random.randn(int(15.3 * L))  # SINAL DE ENTRADA
h = np.random.randn(M)  # FILTRO FIR

# CONVOLUÇÃO USANDO OVERLAP-ADD
y_overlap_add = overlap_add(x, h, N)
plot_signals(x, h, y_overlap_add, "OVERLAP-ADD")

# CONVOLUÇÃO USANDO OVERLAP-SAVE
y_overlap_save = overlap_save(x, h, N)
plot_signals(x, h, y_overlap_save, "OVERLAP-SAVE")

# COMPARATIVO OVERLAP-ADD & OVERLAPE-SAVE 
y_direct = np.convolve(x, h)
plt.figure()
plt.plot(y_direct, label="CONVOLUÇÃO DIRETA")
plt.plot(y_overlap_add, label="OVERLAP-ADD", linestyle="dashed")
plt.plot(y_overlap_save, label="OVERLAP-SAVE", linestyle="dotted")
plt.title("COMPARAÇÃO ENTRE OS MÉTODOS")
plt.xlabel("AMOSTRAS")
plt.ylabel("AMPLITUDE")
plt.legend()
plt.show()

# ===============================================================
# PASSO 2: SIMULAÇÃO COM SINAL DE VOZ
# ===============================================================

# CARREGANDO ARQUIVO DE VOZ QUE JÁ FOI UTILIZADO EM OUTROS TRABALHOS
fs, x_voice = read("amostra.wav")  

# NORMALIZANDO O ÁUDIO PARA EVITAR SATURAÇÃO
x_voice = x_voice / np.max(np.abs(x_voice))

# ADICIONANDO RUÍDO AO SINAL DE VOZ
a1 = 0.5  # Amplitude da primeira senóide
a2 = 0.3  # Amplitude da segunda senóide
f1 = 5500  # Frequência da primeira senóide (Hz)
f2 = 5800  # Frequência da segunda senóide (Hz)

x_voice_noisy = add_sinusoidal_noise(x_voice, a1, f1, a2, f2, fs)

# NORMALIZAR O SINAL COM RUÍDO PARA EVITAR SATURAÇÃO
x_voice_noisy = x_voice_noisy / np.max(np.abs(x_voice_noisy))

# SALVAR O SINAL COM RUÍDO PARA PUDER MOSTRAR
write("voz_com_ruido.wav", fs, np.int16(x_voice_noisy * 32767))  # SALVA ARQUIVO COM RUÍDO

# GARANTIR QUE O ARQUIVO COM RUÍDO SEJA O PROCESSADO NO FILTRO
x_voice_to_filter = x_voice_noisy  # USAR O SINAL COM RUÍDO PARA FILTRAGEM

# FILTRO FIR PARA O SINAL DE VOZ (USANDO FIRWIN EM VEZ DE BLACKMAN)
fc = 5000  # Frequência de corte (Hz) para preservar a fala
h_voice = firwin(M, fc / (fs / 2), window="hamming")
h_voice = h_voice / np.sum(h_voice)  # Normalizar para evitar alterações na amplitude

# VISUALIZAR A RESPOSTA EM FREQUÊNCIA DO FILTRO
w, H = freqz(h_voice, worN=8000, fs=fs)
plt.figure()
plt.plot(w, 20 * np.log10(np.abs(H)))
plt.title("Resposta em Frequência do Filtro FIR")
plt.xlabel("Frequência (Hz)")
plt.ylabel("Magnitude (dB)")
plt.grid()
plt.show()

# FILTRAGEM USANDO OVERLAP-ADD
y_voice = overlap_add(x_voice_to_filter, h_voice, N)

# NORMALIZAR O SINAL FILTRADO PARA SALVAR SEM SATURAÇÃO
y_voice = y_voice / np.max(np.abs(y_voice))

# SALVA ÁUDIO FILTRADO
write("voz_filtrada.wav", fs, np.int16(y_voice * 32767))  

# EXIBIR GRÁFICOS DO SINAL DE VOZ
plot_signals(x_voice, h_voice, y_voice, "SINAL DE VOZ")

# EXIBIR GRÁFICOS COMPARATIVOS DOS SINAIS DE VOZ
plot_signals_comparison(x_voice, x_voice_noisy, y_voice, fs)
