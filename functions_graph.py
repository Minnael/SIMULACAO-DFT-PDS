import numpy as np
import matplotlib.pyplot as plt

# ===============================================================
# FUNÇÕES PARA EXIBIÇÃO DE GRÁFICOS
# ===============================================================

# FUNÇÃO PARA EXIBIR GRÁFICOS DE UM ÚNICO SINAL
def plot_signals(x, h, y, method):
    plt.figure(figsize=(12, 8))

    plt.subplot(3, 1, 1)
    plt.title(f"SINAL DE ENTRADA ({method})")
    plt.plot(x)
    plt.xlabel("AMOSTRAS")
    plt.ylabel("AMPLITUDE")

    plt.subplot(3, 1, 2)
    plt.title("FILTRO (RESPOSTA AO IMPULSO)")
    plt.plot(h)
    plt.xlabel("AMOSTRAS")
    plt.ylabel("AMPLITUDE")

    plt.subplot(3, 1, 3)
    plt.title(f"SINAL DE SAÍDA ({method})")
    plt.plot(y)
    plt.xlabel("AMOSTRAS")
    plt.ylabel("AMPLITUDE")

    plt.tight_layout()
    plt.show()

# FUNÇÃO PARA COMPARAR SINAIS (ORIGINAL, COM RUÍDO E FILTRADO)
def plot_signals_comparison(original, noisy, filtered, fs):
    time_original = np.arange(len(original)) / fs
    time_noisy = np.arange(len(noisy)) / fs
    time_filtered = np.arange(len(filtered)) / fs

    plt.figure(figsize=(15, 10))

    plt.subplot(3, 1, 1)
    plt.title("SINAL ORIGINAL")
    plt.plot(time_original, original)
    plt.xlabel("TEMPO (S)")
    plt.ylabel("AMPLITUDE")

    plt.subplot(3, 1, 2)
    plt.title("SINAL COM RUÍDO")
    plt.plot(time_noisy, noisy)
    plt.xlabel("TEMPO (S)")
    plt.ylabel("AMPLITUDE")

    plt.subplot(3, 1, 3)
    plt.title("SINAL FILTRADO")
    plt.plot(time_filtered, filtered)
    plt.xlabel("TEMPO (S)")
    plt.ylabel("AMPLITUDE")

    plt.tight_layout()
    plt.show()