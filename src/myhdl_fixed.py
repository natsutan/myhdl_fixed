# -*- coding: utf-8 -*-
__author__ = 'mnatsutani'

import myhdl
from myhdl import intbv

# パラメータ	値の型	説明
# W	int(正の値)	全体のビット幅(ワード長)
# I	int	整数部のビット幅、正負の値が指定できる
# Q	sc_q_mode	量子化モード(省略可)
# O	sc_o_mode	オーバーフローモード(省略可)
# N	int	オーバーフロー用ビット数(省略可、Oのためのオプション)
class Signal_fixed(intbv):
    def __init__(self, w, i, q='SC_TRN', o='SC_WRAP', n=0, val=None):
        self.W = w
        self.I = i
        self.Q = q
        self.O = o
        self.N = n
        self.overflow_flag = 0
        min = - (2 ** (self.W-1))
        max = (2 ** (self.W-1)) - 1

        fixed_val = self.calc_fixed_val(val)
        intbv.__init__(self, min=min, max=max, val=fixed_val)

    def calc_fixed_val(self, val):
        fixed = val * (2 ** (self.W - self.I))

        return int(fixed)

    def fixed_mul(self, y):
        None

    def fixed_add(self, y):
        None


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


