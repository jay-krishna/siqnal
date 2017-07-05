"""
    **Author :** *Jay Krishna*

    This module graphs frequency domain plot of the given signal of specified time duration.
"""
from Modules import SignalData

import numpy as np
import matplotlib.pyplot as plt

from Modules import fourier


def SignalFreqPlot(SignalInfo, start, end):
    """
        This function plots frequency domain graph of specified signal from a given start time(inclusive) 
        to a given end time(exclusive).

        Parameters
        ------------------------------
        SignalInfo : object
            Instance of class SignalData.
        start : int
            Start of time(inclusive) from which plotting will start.
        end : int
            End of time(exclusive) from which plotting will end.
    """

    value = SignalInfo.getvalues()
    signal = value[2]

    if(value[1] == ".wav"):
        factor = 1
        startslice = start * factor * int(value[3])
        endslice = end * factor * int(value[3])
        signal_chunk = signal[startslice:endslice, :]
        signal_chunk = signal_chunk.flatten()
        signal_chunk = signal_chunk - 127.5
    elif(value[1] == ".dat"):
        factor = 2
        startslice = start * factor * int(value[3])
        endslice = end * factor * int(value[3])
        signal_chunk = signal[startslice:endslice]
        signal_chunk = signal_chunk - 127.5
    else:
        factor = 1
        startslice = start * factor * int(value[3])
        endslice = end * factor * int(value[3])
        signal_chunk_iq = signal[startslice:endslice]

    if(value[1] != ".txt"):
        signal_chunk_iq = np.empty(
            signal_chunk.shape[0] // 2, dtype=np.complex128)
        signal_chunk_iq.real = signal_chunk[::2]
        signal_chunk_iq.imag = signal_chunk[1::2]

    frequency, transform = fourier.CalcFourier(
        signal_chunk_iq, value[3], value[4])

    plt.rcParams["figure.figsize"] = (16, 6)
    fig = plt.figure()

    ax = fig.add_subplot(111)
    plt.gca().xaxis.grid(True)
    plt.gca().yaxis.grid(True)
    ax.set_title("Freq Domain Plot of Signal")
    ax.set_xlabel('Freq(Hz)')
    ax.set_ylabel('|X(t)|')
    plt.plot(frequency, transform)
    plt.show()
