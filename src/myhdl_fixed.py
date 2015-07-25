# -*- coding: utf-8 -*-
__author__ = 'mnatsutani'
from myhdl import intbv

class Signal_fixed(intbv):

    def __init__(self, w, i, q='SC_TRN', o='SC_WRAP', n=0):
        intbv.__init__(self)
        self.W = w
        self.I = i
        self.Q = q
        self.O = o
        self.N = n



# SC_RND
# SC_RND_ZERO
# SC_RND_MIN_INF
# SC_RND_INF
# SC_RND_CONV
# SC_TRN (デフォルト)
# 3 SC_TRN_ZERO

# SC_SAT
# SC_SAT_ZERO
# SC_SAT_SYM
# SC_WRAP (デフォルト)
# SC_WRAP_SM

# パラメータ	値の型	説明
# W	int(正の値)	全体のビット幅(ワード長)
# I	int	整数部のビット幅、正負の値が指定できる
# Q	sc_q_mode	量子化モード(省略可)
# O	sc_o_mode	オーバーフローモード(省略可)
# N	int	オーバーフロー用ビット数(省略可、Oのためのオプション)
