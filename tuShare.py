#!/usr/bin/python
# -*- coding: utf8 -*-
"""
@version: ??
@author: lihai 
@license: Apache Licence 
@contact: 13142283701 51347294@qq.com 
@software: PyCharm Community Edition
@file: getMP.py
@time: 2018/4/11 10:13
"""
import tushare as ts
import sys
import time
import os


def isFloat(str):
    import re
    value = re.compile(r'^\d+(\.\d+)?$')

    result = value.match(str)
    if result:
        return True
    return False


if __name__ == '__main__':
    try:
        print("#" * 50, "start")
        if len(sys.argv) > 1:
            m = sys.argv[1]
            args = sys.argv[2:]

        print("method:", m)
        method = getattr(ts, m)
        print("args:", args)

        if "--help" in args or "-h" in args:
            # 调用帮助
            help(method)
        else:
            # 运行
            d_args = {}
            for arg in args:
                if "=" in arg:
                    item = arg.split("=")
                    key = item[0]
                    val = item[1]
                    if not key in ['code', 'symbols', 'ktype']:
                        d_args[key] = float(val) if isFloat(val) else val
                    else:
                        d_args[key] = val

            df = method(**d_args)
            if not df.empty:
                print(df.to_string())
                # not none
                outdir = "out"
                if not os.path.exists(outdir):
                    os.makedirs(outdir)

                path = "{0}/{1}.csv".format(outdir, int(round(time.time() * 1000)))  # 毫秒级时间戳
                df.to_csv(path)
                print("out path:", path)
    except Exception as e:
        print("error", e)
    finally:
        print("#" * 50, "end")
        exit()
