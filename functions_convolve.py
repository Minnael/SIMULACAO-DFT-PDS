import numpy as np

# ===============================================================
# FUNÇÕES PARA CÁLCULO DE CONVOLUÇÃO UTILIZANDO FFT (OVERLAP-ADD E OVERLAP-SAVE)
# ===============================================================

# FUNÇÃO PARA CALCULAR A CONVOLUÇÃO USANDO OVERLAP-SAVE
def overlap_save(x, h, N):
    M = len(h)
    L = N - M + 1  # COMPRIMENTO ÚTIL DO SEGMENTO
    x_padded = np.append(np.zeros(M - 1), x)  # PRÉ-PEND ZERO-PADDING AO SINAL DE ENTRADA
    h_padded = np.append(h, np.zeros(N - M))  # ZERO-PADDING AO FILTRO FIR
    H = np.fft.fft(h_padded, N)  # FFT DO FILTRO COM TAMANHO N

    y = []  # ARMAZENAR OS SEGMENTOS DA SAÍDA
    for i in range(0, len(x_padded) - M + 1, L):
        x_segment = x_padded[i:i + N]  # EXTRAI SEGMENTO DE TAMANHO N
        if len(x_segment) < N:  # GARANTE QUE O SEGMENTO TENHA TAMANHO N
            x_segment = np.append(x_segment, np.zeros(N - len(x_segment)))
        X = np.fft.fft(x_segment, N)  # FFT DO SEGMENTO DE ENTRADA
        Y = X * H  # MULTIPLICAÇÃO NO DOMÍNIO DA FREQUÊNCIA
        y_segment = np.fft.ifft(Y).real  # TRANSFORMADA INVERSA PARA O DOMÍNIO DO TEMPO
        y.append(y_segment[M - 1:])  # REMOVE SOBREPOSIÇÃO INICIAL
    return np.concatenate(y)  # CONCATENA TODOS OS SEGMENTOS


# FUNÇÃO PARA CALCULAR A CONVOLUÇÃO USANDO OVERLAP-ADD
def overlap_add(x, h, N):
    M = len(h)
    L = N - M + 1
    x_padded = np.append(x, np.zeros((L - len(x) % L) % L))  
    h_padded = np.append(h, np.zeros(N - M))  
    H = np.fft.fft(h_padded)

    y = np.zeros(len(x_padded) + M - 1)
    for i in range(0, len(x_padded), L):
        x_segment = x_padded[i:i + L]
        x_segment_padded = np.append(x_segment, np.zeros(N - L))
        X = np.fft.fft(x_segment_padded)
        Y = X * H
        y_segment = np.fft.ifft(Y).real
        y[i:i + N] += y_segment
    return y[:len(x) + M - 1]

