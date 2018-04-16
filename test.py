#!/usr/bin/python
# -*- coding: utf8 -*-

import os
import tushare as ts
# os.system("python tuShare.py get_hist_data -h");
# os.system("python tuShare.py get_hist_data code=159915 start=2018-04-01");

# os.system("python tuShare.py shibor_data -h");
# os.system("python tuShare.py shibor_data");
# os.system("python tuShare.py get_sina_dd code=600023 date=2018-04-11 vol=1000")
# print(ts.get_sina_dd("600023","2018-04-11",vol=1000))
os.system("python tuShare.py get_realtime_quotes symbols=159915")
# os.system("python tuShare.py get_sina_dd 600018 date='2018-04-10' vol=1");
