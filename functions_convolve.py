import numpy as np

# ===============================================================
# FUNÇÕES PARA CÁLCULO DE CONVOLUÇÃO UTILIZANDO FFT (OVERLAP-ADD E OVERLAP-SAVE)
# ===============================================================

# FUNÇÃO PARA CALCULAR A CONVOLUÇÃO USANDO OVERLAP-SAVE
def overlap_save(x, h, N):
    M = len(h)
    L = N - M + 1  # COMPRIMENTO ÚTIL DO SEGMENTO
    x_padded = np.append(np.zeros(M - 1), x)  
    h_padded = np.append(h, np.zeros(N - M))  
    H = np.fft.fft(h_padded, N)  # FFT DO FILTRO COM TAMANHO N

    y = []  # ARMAZENAR OS SEGMENTOS DA SAÍDA
    for i in range(0, len(x_padded) - M + 1, L):
        x_segment = x_padded[i:i + N]  
        if len(x_segment) < N:  
            x_segment = np.append(x_segment, np.zeros(N - len(x_segment)))
        X = np.fft.fft(x_segment, N)  
        Y = X * H  
        y_segment = np.fft.ifft(Y).real  
        y.append(y_segment[M - 1:])  
    return np.concatenate(y)  


# FUNÇÃO PARA CALCULAR A CONVOLUÇÃO USANDO OVERLAP-ADD
def overlap_add(x, h, N):
    M = len(h)  # TAMANHO DO FILTRO
    L = N - M + 1 # TAMANHO DO SEGMENTO DE ENTRADA (N - M + 1) PARA EVITAR ALIASING
    x_padded = np.append(x, np.zeros((L - len(x) % L) % L))  
    h_padded = np.append(h, np.zeros(N - M))  
    H = np.fft.fft(h_padded) # REALIZANDO A TRANSFORMADA DE FOURIER DA RESPOSTA AO IMPULSO

    y = np.zeros(len(x_padded) + M - 1)
    for i in range(0, len(x_padded), L): # PERCORRENDO x EM BLOCO DE TAMANHO L
        x_segment = x_padded[i:i + L]
        x_segment_padded = np.append(x_segment, np.zeros(N - L))
        X = np.fft.fft(x_segment_padded)
        Y = X * H
        y_segment = np.fft.ifft(Y).real
        y[i:i + N] += y_segment
    return y[:len(x) + M - 1]

