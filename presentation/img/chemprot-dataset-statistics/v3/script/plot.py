#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Aim: make a plot with the ChemProt dataset statistics.
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

abstracts = np.array([1020, 612, 800])
chemicals = np.array([13017, 8004, 10810])
proteins = np.array([12735, 7563, 10018])
relations = np.array([4157, 2416, 3458])


fig, ax = plt.subplots()
#ax.yaxis.set_major_formatter(FuncFormatter(thousands))

#ffcdcd (original colors)
#cdffcd (original colors)
_ = ax.bar(X - 1.5 * width, abstracts, width, label='Abstracts', color='#d88554') # #ff7f0e #23373b #d88554
_ = ax.bar(X - 0.5 * width, chemicals, width, label='Chemical', color=(0.7686274509803922, 0.3058823529411765, 0.3215686274509804))
_ = ax.bar(X + 0.5 * width, proteins, width, label='Protein', color=(0.3333333333333333, 0.6588235294117647, 0.40784313725490196))
_ = ax.bar(X + 1.5 * width, relations, width, label='Relations', color=(0.2980392156862745, 0.4470588235294118, 0.6901960784313725))
_ = ax.set_yticks(np.arange(0, 15_000, 1_200))

_ = ax.set_xlim(0.0, 6.0)
_ = ax.set_xticks(X)
_ = ax.set_xticklabels(groups)
_ = ax.legend()

fig.set_size_inches(16, 7.5)

#plt.show()

# fig.savefig('001.pdf', bbox_inches='tight', pad_inches=0.0)
fig.savefig('001.pdf', pad_inches=0.5)
plt.clf()
