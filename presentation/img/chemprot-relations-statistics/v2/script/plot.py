#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Aim: make a plot with the ChemProt relations statistics.
#
# Reference:
# https://matplotlib.org/3.2.0/gallery/units/bar_unit_demo.html
#

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns; sns.set()


font_path = '/usr/share/fonts/truetype/lato/Lato-Regular.ttf'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = prop.get_name()
# plt.rcParams.update({'font.size': 22})

# https://matplotlib.org/3.1.0/gallery/ticks_and_spines/custom_ticker1.html
def millions(x, pos):
    return '%1.1f M' % (x / 1_000_000)


def thousands(x, pos):
    return '%1.1f K' % (x / 1_000)


groups = ['Training', 'Development', 'Test']

X = np.array([1, 3, 5])
width = 0.25

r1 = np.array([ 768,  550,  665])
r2 = np.array([2254, 1094, 1661])
r3 = np.array([ 173,  116,  195])
r4 = np.array([ 235,  199,  293])
r5 = np.array([ 727,  457,  644])


fig, ax = plt.subplots()
#ax.yaxis.set_major_formatter(FuncFormatter(thousands))

_ = ax.bar(X - 2 * width, r1, width, label='Activation')
_ = ax.bar(X - 1 * width, r2, width, label='Inhibition')
_ = ax.bar(X + 0 * width, r3, width, label='Agonist')
_ = ax.bar(X + 1 * width, r4, width, label='Antagonist')
_ = ax.bar(X + 2 * width, r5, width, label='Substrate')
_ = ax.set_yticks(np.arange(0, 3_000, 500))

_ = ax.set_xlim(0.0, 6.0)
_ = ax.set_xticks(X)
_ = ax.set_xticklabels(groups)
_ = ax.legend()

fig.set_size_inches(16, 7.5)

#plt.show()

# fig.savefig('001.pdf', bbox_inches='tight', pad_inches=0.0)
fig.savefig('001.pdf', pad_inches=0.5)
plt.clf()
