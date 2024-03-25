#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Aim: make a plot with MEDLINE indexed citations
# (number of publications per year).
# Reference:
# https://www.nlm.nih.gov/bsd/medline_cit_counts_yr_pub.html
# Accessed on September 19, 2022, 10:50.
#

#
# 2022-11-14:
# Last working execution was with Python 3.8.10.
#

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.ticker import FuncFormatter
import numpy as np
import seaborn as sns

#
# To change colors.
# https://stackoverflow.com/questions/25238442/setting-plot-background-colour-in-seaborn
#
# To specify font type.
# https://stackoverflow.com/questions/20753782/default-fonts-in-seaborn-statistical-data-visualization-in-ipython
# https://stackoverflow.com/questions/35668219/how-to-set-up-a-custom-font-with-custom-path-to-matplotlib-global-font/43647344
#
sns.set()

font_path = '/usr/share/fonts/truetype/lato/Lato-Regular.ttf'
font_manager.fontManager.addfont(font_path)
prop = font_manager.FontProperties(fname=font_path)

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = prop.get_name()
plt.rcParams.update({'font.size': 22})


#
# It needs to have two arguments because of FuncFormatter.
# https://matplotlib.org/3.1.0/gallery/ticks_and_spines/custom_ticker1.html
#
#
def millions(x, pos):
    return '%1.1f M' % (x / 1_000_000)


data = np.array([
    [2020, 986_012],
    [2019, 903_184],
    [2018, 866_985],
    [2017, 848_833],
    [2016, 862_858],
    [2015, 878_407],
    [2014, 871_026],
    [2013, 854_128],
    [2012, 811_157],
    [2011, 769_279],
    [2010, 735_005],
    [2009, 707_726],
    [2008, 685_932],
    [2007, 657_649],
    [2006, 634_565],
    [2005, 609_839],
    [2004, 579_041],
    [2003, 549_304],
    [2002, 521_684],
    [2001, 505_770],
    [2000, 485_493],
    [1999, 459_801],
    [1998, 446_844],
    [1997, 432_077],
    [1996, 421_840],
    [1995, 416_454],
    [1994, 407_308],
    [1993, 398_107],
    [1992, 391_789],
    [1991, 388_767],
    [1990, 388_120],
    [1989, 381_394],
    [1988, 365_609],
    [1987, 347_999],
    [1986, 330_454],
    [1985, 318_108],
    [1984, 307_931],
    [1983, 299_016],
    [1982, 285_221],
    [1981, 274_481],
    [1980, 272_538],
    [1979, 274_279],
    [1978, 265_555],
    [1977, 255_745],
    [1976, 249_180],
    [1975, 244_105],
    [1974, 229_807],
    [1973, 225_870],
    [1972, 222_237],
    [1971, 216_614],
    [1970, 211_330],
    [1969, 210_436],
    [1968, 203_701],
    [1967, 186_843],
    [1966, 175_197],
    [1965, 173_135],
    [1964, 158_922],
    [1963, 137_734],
    [1962, 122_645],
    [1961, 117_003],
    [1960, 108_860],
    [1959, 107_786],
    [1958, 107_655],
    [1957, 109_811],
    [1956, 105_228],
    [1955, 106_759],
    [1954, 104_007],
    [1953, 107_678],
    [1952, 106_850],
    [1951, 102_578],
    [1950,  84_099],
])

X, y = data[:,0][::-1], data[:,1][::-1]

fig, ax = plt.subplots()
ax.yaxis.set_major_formatter(FuncFormatter(millions))
_ = ax.set_ylim([0, 1_000_000])
_ = plt.bar(X, y)
# _ = plt.xticks(np.arange(X[0], X[-1], 5))
# _ = plt.xticks(np.arange(X[0], X[-1], 10))
ticks = np.array([1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
_ = plt.xticks(ticks)
_ = plt.xlabel('Year')
_ = plt.ylabel('MEDLINE\ncitation\ncounts', rotation='horizontal', ha='left')
# https://stackoverflow.com/questions/37815976/setting-the-position-of-the-ylabel-in-a-matplotlib-graph
ax.yaxis.set_label_coords(0.065, 0.88)
# fig.set_size_inches(16, 10)
# fig.set_size_inches(16, 9)
# fig.set_size_inches(16, 7.5)
fig.set_size_inches(16, 7.5)
# fig.set_size_inches(16, 7)
# plt.show()
fig.savefig('img.pdf', bbox_inches='tight')
plt.clf()
