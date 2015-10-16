__author__ = 'mnatsutani'

from src.myhdl_fixed import Signal_fixed

val = Signal_fixed(w=9, i=5, q='SC_RND', o='SC_SAT', val=10.25)
print(len(val))
print("val = %s" % bin(val))
