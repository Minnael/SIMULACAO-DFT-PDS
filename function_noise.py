import numpy as np

def add_sinusoidal_noise(signal, a1, f1, a2, f2, fs):
    duration = len(signal) / fs  # DURAÇÃO DO SINAL EM SEGUNDOS
    t = np.linspace(0, duration, len(signal), endpoint=False)  # VETOR DE TEMPO
    noise = a1 * np.cos(2 * np.pi * f1 * t) + a2 * np.cos(2 * np.pi * f2 * t)  # RUÍDO SENOIDAL
    noisy_signal = signal + noise  # ADICIONA O RUÍDO AO SINAL ORIGINAL
    return noisy_signal


