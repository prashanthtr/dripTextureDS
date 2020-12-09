import numpy as np
import math

import synthInterface as SI
from myDrip import MyDrip  # This is "event" synthesizer this pattern synth will use

################################################################################################################
class MyDripPatternSynth(SI.MySoundModel) :

	def __init__(self, cf=440, Q=50, rate_exp=0, irreg_exp=1) :

                SI.MySoundModel.__init__(self)
		#create a dictionary of the parameters this synth will use
                self.__addParam__("cf", 220, 440, cf,
			lambda v :
				self.evSynth.setParam('cf', v))
                self.__addParam__("Q", 0.1, 70, Q,
			lambda v :
                                self.evSynth.setParam('Q', v))
                self.__addParam__("rate_exp", -10, 10, rate_exp)
                self.__addParam__("irreg_exp", .1, 50, irreg_exp)

                self.evSynth=MyDrip(cf,Q)

	'''
		Override of base model method
	'''
	def generate(self,  durationSecs) :
                elist=SI.noisySpacingTimeList(self.getParam("rate_exp"), self.getParam("irreg_exp"), durationSecs)
                return self.elist2signal(elist, durationSecs)


	''' Take a list of event times, and return our signal of filtered pops at those times'''
	def elist2signal(self, elist, sigLenSecs) :
                numSamples=self.sr*sigLenSecs
                sig=np.zeros(sigLenSecs*self.sr)
                for nf in elist :
                        startsamp=int(round(nf*self.sr))%numSamples
                        # create some deviation in center frequency
                        cfsd = 1
                        perturbedf0 = self.getParam("cf")*np.power(2,np.random.normal(scale=cfsd)/12)
                        #perturbedf1 = self.getParam("f1")*np.power(2,np.random.normal(scale=cfsd)/12)

                        self.evSynth.setParam("cf", perturbedf0)
                        #self.evSynth.setParam("f1", perturbedf1)
                        sig = SI.addin(self.evSynth.generate(1), sig, startsamp)

                return sig
