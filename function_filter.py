import numpy as np

def function_filter(h_voice, M, wc):

    for n in range(M):
        if n == (M - 1) // 2:  #EVITANDO DIVISÃO POR ZERO
            h_voice[n] = wc / np.pi
        else:
            h_voice[n] = (np.sin(wc * (n - (M - 1) // 2)) / (np.pi * (n - (M - 1) // 2))) * \
                        (0.42 - 0.5 * np.cos(2 * np.pi * n / (M - 1)) + 0.08 * np.cos(4 * np.pi * n / (M - 1)))