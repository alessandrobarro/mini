import numpy as np
import pywt
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Load the signal
samplerate, data = wavfile.read('Il-barbiere-di-Siviglia-Fígaro.wav')

# Ensure the data is in the correct format (mono)
if len(data.shape) > 1:
    data = data[:, 0]

# Normalize the data
data = data / np.amax(np.abs(data))

# Retrieving time
t = np.linspace(0, len(data) / samplerate, num=len(data))

# Wavelet transform with 2 level decomposition
coeffs = pywt.wavedec(data, wavelet='bior6.8', mode='sym', level=2)
cA2, cD2, cD1 = coeffs

wavfile.write('samplecA2.wav', samplerate, cA2)
wavfile.write('samplecD2.wav', samplerate, cD2)
wavfile.write('samplecD1.wav', samplerate, cD1)

# Reconstruct the signal from the coefficients
reconstructed_signal = pywt.waverec(coeffs, 'bior6.8', 'sym')

wavfile.write('sampler.wav', samplerate, reconstructed_signal)

# Ensure the reconstructed signal is the same length as the original
reconstructed_signal = reconstructed_signal[:len(data)]

# Plotting
plt.figure(figsize=(12, 8))

# Original Signal
plt.subplot(4, 1, 1)
plt.plot(t, data, color='black')
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# Approximation Coefficients at Level 2
plt.subplot(4, 1, 2)
plt.plot(cA2, color='red')
plt.title('Level 2 Approximation Coefficients')
plt.xlabel('Coefficient Index')
plt.ylabel('Coefficient Value')

# Detailed Coefficients at Level 1
plt.subplot(4, 1, 3)
plt.plot(cD1, color='green')
plt.title('Level 1 Detail Coefficients')
plt.xlabel('Coefficient Index')
plt.ylabel('Coefficient Value')

# Reconstructed Signal
plt.subplot(4, 1, 4)
plt.plot(t, reconstructed_signal, color='blue')
plt.title('Reconstructed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.savefig('wavelet_decomposition_reconstruction.png')
plt.show()