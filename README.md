# tushare_cq
tushare command call

tushare挖地兔 命令调用快捷方式

python tuShare.py 调用方法名 [参数1] [参数2]

如：获取实时分笔方法
# 代码
import tushare as ts
df = ts.get_realtime_quotes('159915')

# 命令 
python tuShare.py get_realtime_quotes symbols=159915

# 输出
################################################## start
method: get_realtime_quotes
args: ['symbols=159915']
  name   open pre_close  price   high    low    bid    ask     volume         amount  b1_v   b1_p  b2_v   b2_p  b3_v   b3_p  b4_v   b4_p  b5_v   b5_p  a1_v   a1_p   a2_v   a2_p   a3_v   a3_p  a4_v   a4_p   a5_v   a5_p        date      time    code
0  创业板  1.722     1.721  1.727  1.748  1.714  1.726  1.727  318966300  552584522.492  3284  1.726  5925  1.725  1836  1.724  2155  1.723  6562  1.722  2628  1.727  12176  1.728  16048  1.729  5716  1.730  10350  1.731  2018-04-16  11:16:42  159915
out path: out/1523848603111.csv
################################################## end

其它方法调用同理
