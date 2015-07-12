__author__ = 'mnatsutani'

import myhdl
from src.myhdl_fixed import Signal_fixed

val = Signal_fixed(w=8,i=4, q='SC_RND', o='SC_SAT', val = -2.5)
print(len(val))
print("val = %d" % val)