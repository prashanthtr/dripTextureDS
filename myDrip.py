import numpy as np
#import seaborn as sns
from scipy import signal
import math
#import sys

from synthInterface import MySoundModel

class MyDrip(MySoundModel) :

        def __init__(self, f0=440, f1=880) :
                MySoundModel.__init__(self)
                #create a dictionary of the parameters this synth will use
                self.__addParam__("f0", 100, 2000, f0)
                self.__addParam__("f1", 100, 2000, f1)

        '''
        Override of base model method
        Frequency sweeper for a drip sound
            A = sine wave amplitude
            fs = sample rate (Hz)
            f0 = initial frequency (Hz)
            f1 = final frequency (Hz)
            T_sweep = duration of sweep (s)
        '''
        def generate(self, sigLenSecs):

                # notation for this method
                f0=self.getParam("f0")
                f1 =self.getParam("f1")
                T_sweep = sigLenSecs # Siglensecs is the same as the duration of the sweep
                output = []

                # drip specific parameters
                length = round(sigLenSecs*self.sr) # in samples
                phi = 0;                      # phase accumulator
                f = f0;                       # initial frequency
                delta = 2 * math.pi * f / self.sr     # phase increment per sample
                f_delta = (f1 - f0) / (self.sr * T_sweep) # instantaneous frequency increment per sample
                output = np.zeros(length)

                for index in range(len(output)):

                        A = 1
                        val = A * math.sin(phi);    # output sample value for current sample
                        phi += delta;             # increment phase accumulator
                        f += f_delta;             # increment instantaneous frequency
                        delta = 2 * math.pi * f / self.sr;  # re-calculate phase increment
                        output[index] = val

                return output
